from Models.RegistrationData import RegistrationData
from Models.Enums.userUniqueFields import UserUniqueFields as uuf
from Models.Enums.RegistrationFields import RegistrationFields as rf
from Exceptions.RegistrationErrors import InvalidEmailFormatError, AgeInvalidError
from Exceptions.DatabaseErrors import DuplicateError
from Models.User import User
from datetime import date
import re

class RegistrationService:
    def __init__(self, repository):
        self.repository = repository

    """
        Check if User email is in valid form
        Check if User age is between 18 - 100 years
        Creates the User Object and pass the object to user repository 
    """
    def register(self, data: RegistrationData):
        if not RegistrationService.is_email_valid(data.email):
            raise InvalidEmailFormatError()
        if not RegistrationService.is_age_valid(data.dob):
            raise AgeInvalidError()
        
        user = User(data.name, data.dob, data.gender, data.email, data.mobNo, data.address, data.aadharNo, data.panNo)
        try:
            self.repository.add_user(user)
        except DuplicateError as error:
            user_registration_correspondence = {
                uuf.PAN : rf.PAN,
                uuf.AADHAR : rf.AADHAR,
                uuf.EMAIL : rf.EMAIL,
                uuf.MOBNO : rf.MOBNO
            }
            raise DuplicateError(f"{user_registration_correspondence[error.field].value} already in use! Try again.", user_registration_correspondence[error.field]) from error
        
            

    @staticmethod
    def is_email_valid(email):
        pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
        return bool(re.fullmatch(pattern, email))
    
    @staticmethod
    def is_age_valid(dob: date):
        today_date = date.today()
        age = today_date.year - dob.year
        if( (today_date.month, today_date.day) < (dob.month, dob.day) ):
            age-=1
        return bool(age>=18 and age<=100)



    
          