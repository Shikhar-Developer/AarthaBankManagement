from Models.Enums.constants import Roles

class RolesService:
    def __init__(self, sessionContext, service = None):
        self.sessionContext = sessionContext
        self.service = service
    
    def updateRole(self, role:Roles):
        self.sessionContext.setRole(role)