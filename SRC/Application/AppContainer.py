from Session.SessionContext import SessionContext
from Infrastructure.Persistence.MySQLUserRepository import MySQLUserRepository
from Infrastructure.Database.config import Connection
from Infrastructure.Security.BcryptHasher import BcryptHasher
from Auth.authContainer import AuthContainer

class AppContainer:
    def __init__(self):
        
        # Connection Object: DataBase Connection
        self.conobj = Connection.getConnector()
 
        #Session Context: Session Context
        self.sessionContext = SessionContext(1)
 
        #Repository : User Respository
        self.userRepository = MySQLUserRepository(self.conobj)

        #Password hasher
        self.passwordHasher = BcryptHasher()

        #AuthContainer Intialization
        self.authContainer = AuthContainer(self.userRepository, self.sessionContext, self.passwordHasher) 


    def getStartWindow(self):
        return self.authContainer.getMainWindow()

    
