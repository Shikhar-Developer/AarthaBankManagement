from Domain.Enum.constants import Page, Roles

class RolesController:
    def __init__(self, view, navigationMethod, service, sessionContext):
        self.view = view
        self.navigate = navigationMethod
        self.service = service
        self.sessionContext = sessionContext
        self.moduleTransiton = None

    def setup(self):
        self.view.on_next_button_clicked(self.toDashBoard)
        self.view.on_view_shown(self.sendRoles)

    def setTransitionMethod(self, callback):
        self.moduleTransiton = callback
    
    def toDashBoard(self):
        role = self.view.choice()
        if not role:
            self.view.show_error_message("Please choose a role")
            return
        
        #Cleanup
        self.view.removeRoles()
        self.service.updateRole(role)
        
        #Transition To requested Dashboard
        self.moduleTransiton(role)
        

    def sendRoles(self):
        self.view.setRoles(self.sessionContext.available_roles)

