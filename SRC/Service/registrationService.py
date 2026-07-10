from Domain.DTO.RegistrationData import RegistrationData
from Domain.Enum.constants import RegistrationFields as rf, UserUniqueFields as uuf
from Infrastructure.Exceptions.DatabaseErrors import DuplicateError
from Domain.Models.User import User

class RegistrationService:
    def __init__(self, repository):
        self.repository = repository

    def register(self, data: RegistrationData):
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


# Now User doesn't let wrong user get created! 
            




    
          