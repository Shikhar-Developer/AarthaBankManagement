from Domain.Enum.constants import Roles
from PySide6.QtWidgets import QMainWindow

class ApplicationCoordinator:
    def __init__(self, authContainer, adminContainer, customerContainer):
        self.authContainer = authContainer
        self.adminContainer = adminContainer
        self.customerContainer = customerContainer
    
    def transitionTo(self, role):
        if(role == Roles.ADMIN):
            self.authMainWindow = self.authContainer.getMainWindow()
            self.adminMainWindow = QMainWindow()
            # adminMainWindow = self.adminContainer.getMainWindow()

            self.authMainWindow.hide()
            self.adminMainWindow.show()

        if(role == Roles.CUSTOMER):
            pass
        if(role == Roles.BRANCH_MANAGER):
            pass

#Module Transition:- AppContainer calls setTranitionTo method to container then it sends the method to Controller responsible for immediate change.