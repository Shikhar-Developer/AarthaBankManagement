from Infrastructure.Exceptions.DatabaseErrors import RecordNotFoundError 
from Domain.Exceptions.AuthenticationErrors import UserNotFoundError
from Domain.Exceptions.AuthenticationErrors import IncorrectCredentialsError
from Security.passwordHasher import PasswordHasher
from Domain.Enum.constants import Roles
from datetime import datetime

class AuthenticationService:
    def __init__(self, repository, passwordHasher:PasswordHasher | None, sessionContext=None,):
        self.repository = repository
        self.sessionContext = sessionContext
        self.passwordHasher = passwordHasher
        
    def getUserId(self, username, password):
        try:
            authDetails = self.repository.find_by_username(username)
            if not self.passwordHasher.verifyPassword(password, authDetails.Password_hash):
                raise IncorrectCredentialsError("Incorrect username or password!")
            return authDetails.UserId
        except RecordNotFoundError as error:
            raise UserNotFoundError(error.msg) from error

    def login(self, username, password):
        uId   = self.getUserId(username, password)
        roles = self.repository.get_user_role(uId) # User-role as a tuple of tuple
        userRole = tuple(Roles(role[0]) for role in roles)
        self.sessionContext.startSession(uId, userRole, datetime.now())
        


        
