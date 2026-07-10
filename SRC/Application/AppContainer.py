from Session.SessionContext import SessionContext
from Infrastructure.Persistence.MySQLUserRepository import MySQLUserRepository
from Infrastructure.Database.config import Connection
from Infrastructure.Security.BcryptHasher import BcryptHasher
from Auth.authContainer import AuthContainer
from Application.ApplicationCoordinator import ApplicationCoordinator

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

        #Application Coordinator
        self.appCoordinator = ApplicationCoordinator(self.authContainer, None, None)

        self.authContainer.setTransitionMethod(self.appCoordinator.transitionTo)


    def getStartWindow(self):
        return self.authContainer.getMainWindow()

    
