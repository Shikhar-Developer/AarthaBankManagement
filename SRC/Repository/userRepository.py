from Domain.Models.User import User
from Domain.Models.AuthUser import AuthUser
import mysql.connector as sqltor
from Domain.Enum.constants import UserUniqueFields as uuf
from Infrastructure.Exceptions.DatabaseErrors import DuplicateError, DatabaseError, RecordNotFoundError
from datetime import date

class UserRepository:
    def __init__(self, conobj):
        self.conobj = conobj

    def find_by_username(self, username):
        cursor = self.conobj.cursor()
        qry = "SELECT USER_ID, PASSWORD_HASH FROM USERAUTH WHERE USERNAME = %s"
        try:
            cursor.execute(qry, (username,))
            result = cursor.fetchone()
            if not result:
                raise RecordNotFoundError("No user was found!")
            return AuthUser(Username=username, UserId=result[0], Password_hash=result[1])
        except sqltor.Error as error:
            raise DatabaseError(str(error))
        finally:
            cursor.close()
            
    def get_user_role(self, uid):
        cursor = self.conobj.cursor()
        qry = "SELECT R.ROLE_NAME FROM USER_ROLE UR JOIN ROLE R ON UR.ROLE_ID = R.ROLE_ID JOIN USER U ON U.USER_ID = UR.USER_ID WHERE UR.USER_ID = %s AND U.STATUS = 'VERIFIED'"
        try:
            cursor.execute(qry, (uid,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except sqltor.Error as error:
            raise DatabaseError(str(error)) from error
        finally:
            cursor.close()

    def add_user(self, user:User):
        cursor = self.conobj.cursor()

        try:
            qrystr = "INSERT INTO USER (NAME, DOB, GENDER, EMAIL, MOBILE_NUMBER, ADDRESS, AADHAR_NUMBER, PAN_NUMBER) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
            cursor.execute(qrystr, (user.name, user.dob, user.gender, user.email, user.mobno, user.address, user.aadharNumber, user.panNumber))
            self.conobj.commit()
        except sqltor.IntegrityError as error:
            self.conobj.rollback()
            if error.errno == 1062: #Duplicate error code
                if "UNIQUE_MOBILENUMBER_USER" in error.msg:
                    raise DuplicateError("Mobile number is duplicate!", uuf.MOBNO) from error
                if "UNIQUE_EMAIL_USER" in error.msg:
                    raise DuplicateError("Email is duplicate!", uuf.EMAIL) from error
                if "UNIQUE_AADHARNUMBER_USER" in error.msg:
                    raise DuplicateError("Aadhar number is duplicate!", uuf.AADHAR) from error
                if "UNIQUE_PANNUMBER_USER" in error.msg:
                    raise DuplicateError("PAN number is duplicate!", uuf.PAN) from error
            else:
                raise DatabaseError("Database Operation failed!") from error
        except sqltor.Error as error:
            raise DatabaseError(str(error)) from error
        finally:
            cursor.close()


