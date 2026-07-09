from PySide6.QtWidgets import QMainWindow, QStackedWidget, QWidget
from Models.Enums.constants import Page
from Auth.UI.welcomePage import WelcomePage 
from Auth.UI.registrationPage import RegistrationPage
from Auth.UI.loginPage import LoginPage
from Auth.UI.rolesPage import RolesPage

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        #intializing all pages
        self.welcomePage = WelcomePage()
        self.registrationPage = RegistrationPage()
        self.loginPage = LoginPage()
        self.rolePage = RolesPage()
        self.adminDashBoard = QWidget()
        self.customerDashBoard = QWidget()
        self.branchManagerDashBoard = QWidget()

        #A fast enum based Widget LookUp
        self.pages = self.createLookUp()

        #Creating Stack with pages stacked over one another
        self.stack = QStackedWidget()
        for page in self.pages:
            self.stack.addWidget(self.pages[page])

        self.setCentralWidget(self.stack)
        self.stack.setCurrentWidget(self.welcomePage)

    def createLookUp(self):
        return {
            Page.WELCOME                    : self.welcomePage,
            Page.REGISTRATION               : self.registrationPage,
            Page.LOGIN                      : self.loginPage,
            Page.ROLE                       : self.rolePage,
            Page.CUSTOMER_DASHBOARD         : self.customerDashBoard,
            Page.ADMIN_DASHBOARD            : self.adminDashBoard,
            Page.BRANCH_MANAGER_DASHBOARD   : self.branchManagerDashBoard
        }

    def changePage(self, page: Page):
        self.stack.setCurrentWidget(self.pages[page])
