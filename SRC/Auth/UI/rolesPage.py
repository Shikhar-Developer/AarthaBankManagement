from PySide6.QtWidgets import QWidget, QRadioButton, QPushButton, QVBoxLayout, QLabel, QMessageBox 
from PySide6.QtCore import Signal, Qt

from Domain.Enum.constants import Roles

class RolesPage(QWidget):
    view_shown_signal = Signal()

    def __init__(self):

        #Calling the constructor because of custom constructor
        super().__init__()
        self.roles = ()

        #Title: label
        self.title = QLabel("Select a Role")
        self.title.setStyleSheet("font-size: 20px; font-weight: 700;")

        #SubTitle
        self.subtitle = QLabel("Choose a Role to continue to Dashboard")
        # self.title.setStyleSheet("margin-bottom:10px;")

        #RadioButton
        self.customerRadioBtn = QRadioButton("Customer")
        self.adminRadioBtn = QRadioButton("Admin")
        self.branchmanagerRadioBtn = QRadioButton("Branch Manager")

        self.radioButtons = {
            Roles.CUSTOMER : self.customerRadioBtn,
            Roles.ADMIN : self.adminRadioBtn,
            Roles.BRANCH_MANAGER :self.branchmanagerRadioBtn
        }

        #Will Later hold radioButtons
        self.radioLayout = QVBoxLayout() #radioLayout
        self.radioLayout.setSpacing(5)

        #Next Button
        self.nextBtn = QPushButton("Next")
        self.nextBtn.setStyleSheet("max-height: 20px; min-height: 20px; min-width: 150px; max-height: 200px; padding: 12px;")

        self.centralWidget = QWidget()
        self.centralWidget.setFixedWidth(400)
        self.centralLayout = QVBoxLayout(self.centralWidget)
        self.centralLayout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addWidget(self.subtitle, alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralLayout.addLayout(self.radioLayout)
        self.centralLayout.addWidget(self.nextBtn, alignment=Qt.AlignmentFlag.AlignCenter)

        #Overall layout
        self.overallLayout = QVBoxLayout(self)
        self.overallLayout.addWidget(self.centralWidget, alignment = Qt.AlignmentFlag.AlignCenter)
        

    def showEvent(self, event):
        self.view_shown_signal.emit()
        return super().showEvent(event)

    def on_next_button_clicked(self, callback):
        self.nextBtn.clicked.connect(callback)
    
    def on_view_shown(self, callback):
        self.view_shown_signal.connect(callback)

    def setRoles(self, roles):
        for role in roles:
            self.radioLayout.addWidget(self.radioButtons[role])
    
    def removeRoles(self):
        for key in self.radioButtons:
            self.radioLayout.removeWidget(self.radioButtons[key])

    def choice(self):
        for role in self.radioButtons:
            if(self.radioButtons[role].isChecked()):
                return role
        return None

    def show_error_message(self, msg):
        self.subtitle.setText(msg)
        QMessageBox.warning(
            None,
            "Warning",
            msg
        )




    
        





