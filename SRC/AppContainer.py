from UI.MainWindow import MainWindow
from Controller.welcomePageController import WelcomeController
from Controller.navigationController import navController
from Controller.registrationController import RegistrationController
from Service.registrationService import RegistrationService
from Repository.userRepository import UserRepository
import wiring
from Models.Enums.Pages import Page
from Database.config import Connection

class Container:
    def __init__(self):
        
        # Get a Connection Object
        self.conobj = Connection.getConnector()

        #Get a main window
        self.mainWindow = MainWindow()

        #Repository
        self.registrationRepository = UserRepository(self.conobj)

        #Service
        self.registrationService = RegistrationService(self.registrationRepository)

        #Controller
        self.navigationController = navController(self.mainWindow)
        
        self.welcomePageController = WelcomeController(
            self.mainWindow.pages[Page.WELCOME], 
            self.navigationController.navigate
        )
        
        self.registrationController = RegistrationController(
            self.mainWindow.pages[Page.REGISTRATION],
            self.navigationController.navigate, 
            self.registrationService
        )

        wiring.configureControllers(self)

    def getMainWindow(self):
        return self.mainWindow
