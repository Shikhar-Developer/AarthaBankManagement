from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()

        # Welcome Label at the top
        self.welcomeLabel = QLabel("Welcome")
        self.welcomeLabel.setStyleSheet("font-size:20px; font-weight:700px")

        #Buttons on Welcome page
        self.loginBtn = QPushButton("Login")
        self.registerBtn = QPushButton("Register")

        #Button Beautification
        self.loginBtn.setStyleSheet("min-width: 100px; max-width: 150px; max-height: 40px;")
        self.registerBtn.setStyleSheet("min-width: 100px; max-width: 150px; max-height: 40px;")


        #Widget carrying a Horizontal Layout carrying the buttons
        self.buttonWidget = QWidget()
        hLayout = QHBoxLayout(self.buttonWidget)
        hLayout.addWidget(self.loginBtn)
        hLayout.addWidget(self.registerBtn)

        #Vertical Layout carrying label and buttonWidget
        layout = QVBoxLayout(self)
        layout.addWidget(self.welcomeLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.buttonWidget)

    def loginBtnClicked(self, callback):
        self.loginBtn.clicked.connect(callback)

    def registerBtnClicked(self, callback):
        self.registerBtn.clicked.connect(callback)


    