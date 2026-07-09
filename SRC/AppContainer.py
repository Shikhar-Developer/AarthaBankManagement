from Auth.UI.MainWindow import MainWindow

from Session.SessionContext import SessionContext

from Auth.Controller.welcomePageController import WelcomeController
from Auth.Controller.navigationController import navController
from Auth.Controller.registrationController import RegistrationController
from Auth.Controller.loginController import LoginController
from Auth.Controller.rolesController import RolesController

from Service.registrationService import RegistrationService
from Service.AuthenticationService import AuthenticationService
from Service.RolesService import RolesService

from Repository.userRepository import UserRepository

import wiring
from Models.Enums.constants import Page
from Database.config import Connection

class Container:
    def __init__(self):
        
        # Get a Connection Object
        self.conobj = Connection.getConnector()

        #Get a main window
        self.mainWindow = MainWindow()

        #Create a Session Context
        self.sessionContext = SessionContext(1)

        #Repository
        self.userRepository = UserRepository(self.conobj)

        #Service
        self.registrationService = RegistrationService(self.userRepository)
        self.loginService = AuthenticationService(self.userRepository, self.sessionContext)
        self.rolesService = RolesService(self.sessionContext, None)

        #Controller
        self.navigationController = navController(self.mainWindow.changePage)
        
        self.welcomePageController = WelcomeController(
            self.mainWindow.pages[Page.WELCOME], 
            self.navigationController.navigate
        )
        
        self.registrationController = RegistrationController(
            self.mainWindow.pages[Page.REGISTRATION],
            self.navigationController.navigate, 
            self.registrationService
        )

        self.loginController = LoginController(
            self.mainWindow.pages[Page.LOGIN],
            self.navigationController.navigate,
            self.loginService,
            self.sessionContext
        )

        self.rolesController = RolesController(
            self.mainWindow.pages[Page.ROLE],
            self.navigationController.navigate,
            self.rolesService,
            self.sessionContext
        )

        wiring.configureControllers(self)

    def getMainWindow(self):
        return self.mainWindow

    
