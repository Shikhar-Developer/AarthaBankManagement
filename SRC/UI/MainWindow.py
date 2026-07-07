from PySide6.QtWidgets import QMainWindow, QStackedWidget
from UI.pages.welcomePage import WelcomePage 
from UI.pages.signupPage import SignupPage

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        #intializing all pages
        self.welcomePage = WelcomePage()
        self.signupPage = SignupPage()

        #Creating Stack with pages stacked over one another
        self.stack = QStackedWidget()
        self.stack.addWidget(self.welcomePage)
        self.stack.addWidget(self.signupPage)

        self.setCentralWidget(self.stack)
        self.stack.setCurrentWidget(self.signupPage)
 

