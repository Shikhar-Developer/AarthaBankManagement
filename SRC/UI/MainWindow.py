from PySide6.QtWidgets import QMainWindow, QStackedWidget
from Models.Enums.Pages import Page
from UI.pages.welcomePage import WelcomePage 
from UI.pages.registrationPage import RegistrationPage
from UI.pages.loginPage import LoginPage

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        #intializing all pages
        self.welcomePage = WelcomePage()
        self.registrationPage = RegistrationPage()
        self.loginPage = LoginPage()

        #A fast enum based Widget LookUp
        self.pages = self.createLookUp()

        #Creating Stack with pages stacked over one another
        self.stack = QStackedWidget()
        for page in self.pages:
            self.stack.addWidget(self.pages[page])
        # self.stack.addWidget(self.welcomePage)
        # self.stack.addWidget(self.registrationPage)

        self.setCentralWidget(self.stack)
        self.stack.setCurrentWidget(self.welcomePage)

    def createLookUp(self):
        return {
            Page.WELCOME       : self.welcomePage,
            Page.REGISTRATION  : self.registrationPage,
            Page.LOGIN         : self.loginPage
        }

    def changePage(self, page: Page):
        self.stack.setCurrentWidget(self.pages[page])
 

