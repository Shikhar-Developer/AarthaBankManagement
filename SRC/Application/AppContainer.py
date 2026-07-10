from Session.SessionContext import SessionContext
from Repository.userRepository import UserRepository
from Infrastructure.Database.config import Connection
from Auth.authContainer import AuthContainer

class AppContainer:
    def __init__(self):
        
        # Connection Object: DataBase Connection
        self.conobj = Connection.getConnector()
 
        #Session Context: Session Context
        self.sessionContext = SessionContext(1)
 
        #Repository : User Respository
        self.userRepository = UserRepository(self.conobj)
 
        #AuthContainer Intialization
        self.authContainer = AuthContainer(self.userRepository, self.sessionContext) 


    def getStartWindow(self):
        return self.authContainer.getMainWindow()

    
