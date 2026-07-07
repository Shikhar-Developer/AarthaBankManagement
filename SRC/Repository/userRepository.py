from Models.User import User
import mysql.connector as sqltor
from Models.Enums.userUniqueFields import UserUniqueFields as uuf
from Exceptions.DatabaseErrors import DuplicateError, DatabaseError
from datetime import date

class UserRepository:
    def __init__(self, conobj):
        self.conobj = conobj

    def add_user(self, user:User):
        cursor = self.conobj.cursor()

        try:
            qrystr = "INSERT INTO USER (USER_ID, NAME, DOB, GENDER, EMAIL, MOBILE_NUMBER, ADDRESS, AADHAR_NUMBER, PAN_NUMBER) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)" 
            cursor.execute(qrystr, (1,user.name, date.today(), "Male", user.email, user.mobno, user.address, user.aadharNumber, user.panNumber))
            # cursor.execute(qrystr, (user.name, user.dob, user.gender, user.email, user.mobno, user.address, user.aadharNumber, user.panNumber))
            print("Hi there")
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
            print(str(error))
            raise DatabaseError("Database Operation failed!") from error
        finally:
            cursor.close()


