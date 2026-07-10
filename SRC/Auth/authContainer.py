from Auth.UI.MainWindow import MainWindow

from Service.AuthenticationService import AuthenticationService
from Service.registrationService import RegistrationService
from Service.RolesService import RolesService

from Auth.Controller.navigationController import navController
from Auth.Controller.loginController import LoginController
from Auth.Controller.registrationController import RegistrationController
from Auth.Controller.rolesController import RolesController
from Auth.Controller.welcomePageController import WelcomeController

from Domain.Enum.constants import Page


class AuthContainer:
    def __init__(self, userRepository, sessionContext, passwordHasher):
        #Get a main window
        self.mainWindow = MainWindow()

        #Service
        self.registrationService = RegistrationService(userRepository)
        self.loginService = AuthenticationService(userRepository, passwordHasher, sessionContext)
        self.rolesService = RolesService(sessionContext, None)

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
            sessionContext
        )

        self.rolesController = RolesController(
            self.mainWindow.pages[Page.ROLE],
            self.navigationController.navigate,
            self.rolesService,
            sessionContext
        )

        self.configureControllers()

    def getMainWindow(self):
        return self.mainWindow
    
    def setTransitionMethod(self, callback):
        self.rolesController.setTransitionMethod(callback)

    def configureControllers(self):
        self.welcomePageController.setUp()
        self.registrationController.setup()
        self.loginController.setup()
        self.rolesController.setup()

