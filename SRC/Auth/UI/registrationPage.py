from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QFormLayout, QDateEdit, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QMessageBox
from PySide6.QtCore import Qt, QDate
from Models.Enums.constants import RegistrationFields
from Auth.UI.Widgets.SequentialMaskedWidgets import MaskedLineEdit

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()

        #Page header
        self.title = QLabel("Sign-Up")

        #Inputs
        self.nameInput     = QLineEdit()
        self.genderInput   = QComboBox(); self.genderInput.addItems(["Male", "Female", "Other"])
        self.dobInput      = QDateEdit(calendarPopup = True)
        self.emailInput    = QLineEdit()
        self.mobNoInput    = MaskedLineEdit(startPosition=4)
        self.addressInput  = QLineEdit()
        self.aadharNoInput = MaskedLineEdit()
        self.panNoInput    = MaskedLineEdit()

        # Dictionary conatining all Widgets mapped to their Enums names for ease of Access
        self.Inputs = self.createLookUp()           
        

        #Input masking for better input
        self.nameInput.setMaxLength(50)
        self.emailInput.setMaxLength(100)
        self.mobNoInput.setInputMask(r"+\91-9999999999;_")
        self.addressInput.setMaxLength(255)
        self.aadharNoInput.setInputMask("9999-9999-9999;_")
        self.panNoInput.setInputMask(">AAAAA9999A;_")


        #Form Layout to get Input
        formlayout  =  QFormLayout()
        formlayout.addRow("Name: ", self.nameInput)
        formlayout.addRow("Gender: ", self.genderInput)
        formlayout.addRow("Date of Birth: ", self.dobInput)
        formlayout.addRow("Email: ", self.emailInput)
        formlayout.addRow("Mobile number: ", self.mobNoInput)
        formlayout.addRow("Permanent Address: ", self.addressInput)
        formlayout.addRow("Aadhar Number: ", self.aadharNoInput)
        formlayout.addRow("Pan Number: ", self.panNoInput)


        #Submit Button
        self.submitBtn = QPushButton("Submit")
        self.backBtn = QPushButton("Back")

        #Button-Beautification
        self.submitBtn.setStyleSheet("min-width: 100px; max-width: 150px; max-height:40px")
        self.backBtn.setStyleSheet("min-width: 100px; max-width: 150px; max-height:40px")


        #Horizontal layout holding the button
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.submitBtn)
        horizontalLayout.addWidget(self.backBtn)



        #Final Layout holding both form and button layouts
        finalLayout = QVBoxLayout(self)
        finalLayout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        finalLayout.addLayout(formlayout)
        finalLayout.addLayout(horizontalLayout)


    def createLookUp(self):
        return {
            RegistrationFields.NAME   : self.nameInput,
            RegistrationFields.GENDER : self.genderInput,
            RegistrationFields.DOB    : self.dobInput,
            RegistrationFields.EMAIL  : self.emailInput,
            RegistrationFields.MOBNO  : self.mobNoInput,
            RegistrationFields.ADDRESS: self.addressInput,
            RegistrationFields.AADHAR : self.aadharNoInput,
            RegistrationFields.PAN    : self.panNoInput
        }
    
    def submitBtnClicked(self, callback):
        self.submitBtn.clicked.connect(callback)

    def backBtnClicked(self, callback):
        self.backBtn.clicked.connect(callback)
    
    def getData(self):
        return {
            RegistrationFields.NAME   : self.nameInput.text(),
            RegistrationFields.GENDER : self.genderInput.currentText(),
            RegistrationFields.DOB    : self.dobInput.date(),
            RegistrationFields.EMAIL  : self.emailInput.text(),
            RegistrationFields.MOBNO  : self.mobNoInput.text(),
            RegistrationFields.ADDRESS: self.addressInput.text(),
            RegistrationFields.AADHAR : self.aadharNoInput.text(),
            RegistrationFields.PAN    : self.panNoInput.text()
        }
    
    

    def clearFields(self, feilds):
        for field in feilds:
            widget = self.Inputs[field]
            match (field):
                case (RegistrationFields.GENDER):
                    widget.setCurrentIndex(0)
                case(RegistrationFields.DOB):
                    widget.setDate(QDate(2000, 1, 1))
                case _:
                    widget.clear()

    def show_error_message(self, msg):
        QMessageBox.warning(None, "Duplicate fields", msg)

    def show_confirmation(self, msg):
        QMessageBox.information(None, "Success", msg)

    def closeApp(self):
        QApplication.quit()
        
        


