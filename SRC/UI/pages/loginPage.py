from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class LoginPage(QWidget):
    def __init__(self):
        #Super class Constructor
        super().__init__()

        #QPushButton Login
        self.loginBtn = QPushButton("Login")
        self.loginBtn.setStyleSheet("max-height:40px; min-height:35px; max-width:150px; min-width:100px; border: 1px solid gray; border-radius: 6px; padding: 5px 10px;QPushButton:hover{border: 2px solid gray;}")

        # Login Page - Welcome Back Label
        self.welcomeLabel = QLabel("Welcome Back!")

        #Central Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.welcomeLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loginBtn, alignment=Qt.AlignmentFlag.AlignCenter)




