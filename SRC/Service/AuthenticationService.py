from Infrastructure.Exceptions.DatabaseErrors import RecordNotFoundError 
from Domain.Exceptions.AuthenticationErrors import UserNotFoundError, IncorrectCredentialsError
from Domain.Models.AuthUser import AuthUser
from Domain.Enum.constants import Roles
from datetime import datetime
import bcrypt

class AuthenticationService:
    def __init__(self, repository, sessionContext=None):
        self.repository = repository
        self.sessionContext = sessionContext

    def validateUser(self, inputPassword, password_hash):
        inputBytes = inputPassword.encode("utf-8")
        passwordBytes = password_hash.encode("utf-8")
        if not bcrypt.checkpw(inputBytes, passwordBytes):
            raise IncorrectCredentialsError("Incorrect Email or Password")
        
    def getUserId(self, username, password):
        try:
            authDetails = self.repository.find_by_username(username)
            self.validateUser(password, authDetails.Password_hash)
            return authDetails.UserId
        except RecordNotFoundError as error:
            raise UserNotFoundError(error.msg) from error

    def login(self, username, password):
        uId   = self.getUserId(username, password)
        roles = self.repository.get_user_role(uId) # User-role as a tuple of tuple
        userRole = tuple(Roles(role[0]) for role in roles)
        self.sessionContext.startSession(uId, userRole, datetime.now())
        


        
