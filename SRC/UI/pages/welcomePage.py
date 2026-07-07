from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()

        # Welcome Label at the top
        self.welcomeLabel = QLabel("Welcome")

        #Buttons on Welcome page
        self.loginBtn = QPushButton("Login")
        self.signUpBtn = QPushButton("Signup")

        #Button Beautification
        self.loginBtn.setStyleSheet("min-width: 100px; max-width: 150px; max-height: 40px;")
        self.signUpBtn.setStyleSheet("min-width: 100px; max-width: 150px; max-height: 40px;")


        #Widget carrying a Horizontal Layout carrying the buttons
        self.buttonWidget = QWidget()
        hLayout = QHBoxLayout(self.buttonWidget)
        hLayout.addWidget(self.loginBtn)
        hLayout.addWidget(self.signUpBtn)

        #Vertical Layout carrying label and buttonWidget
        layout = QVBoxLayout(self)
        layout.addWidget(self.welcomeLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.buttonWidget)


    