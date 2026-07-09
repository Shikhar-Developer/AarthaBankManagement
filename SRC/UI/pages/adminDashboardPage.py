from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class AdminDashBoard(QWidget):
    def __init__(self):
        # Calling Super contructors
        super().__init__()

        self.title = QLabel("Admin Dashboard")
        self.title.setStyleSheet("font-size: 20px; font-weight: 700")
        self.subtitle = QLabel("United Admin Workflow")
        self.subtitle.setStyleSheet("font-size:12px; font-weight:200")
        
