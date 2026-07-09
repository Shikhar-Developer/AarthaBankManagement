from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QMessageBox, QApplication
from PySide6.QtCore import Qt
from Models.Enums.constants import LoginFields


class LoginPage(QWidget):
    def __init__(self):
        #Super class Constructor
        super().__init__()

        # Login Page - Welcome Back Label
        self.welcomeLabel = QLabel("Welcome Back!")
        self.welcomeLabel.setStyleSheet("font-size: 20px; font-weight:700;")

        # Credentials
        self.usernameInput = QLineEdit(placeholderText="Enter Username")
        self.passwordInput = QLineEdit(placeholderText="Enter Password", echoMode=QLineEdit.EchoMode.Password)
        self.usernameInput.setStyleSheet("max-height:40px; min-height: 40px; max-width:250px; min-width:200px;")
        self.passwordInput.setStyleSheet("max-height:40px; min-height: 40px; max-width:250px; min-width:200px;")


        #QPushButton Login
        self.loginBtn = QPushButton("Login")
        self.loginBtn.setStyleSheet("max-height:40px; min-height: 40px; max-width:150px; min-width:100px;")

        

        #Central Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.welcomeLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.usernameInput, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.passwordInput, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loginBtn, alignment=Qt.AlignmentFlag.AlignCenter)

    def on_login_button_clicked(self, callback):
        self.loginBtn.clicked.connect(callback)

    def clearfields(self):
        self.usernameInput.clear()
        self.passwordInput.clear()

    def getCredentials(self):
        return {
            LoginFields.USERNAME : self.usernameInput.text(),
            LoginFields.PASSWORD : self.passwordInput.text()
        }
    
    def show_error_message(self, msg):
        QMessageBox.warning(
            None,
            "Error Occured!",
            msg
        )

    def closeApp(self):
        QApplication.quit()
        
        



