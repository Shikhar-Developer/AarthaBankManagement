from Models.Enums.constants import Page, Roles

class RolesController:
    def __init__(self, view, navigationMethod, service, sessionContext):
        self.view = view
        self.navigate = navigationMethod
        self.service = service
        self.sessionContext = sessionContext

    def setup(self):
        self.view.on_next_button_clicked(self.toDashBoard)
        self.view.on_view_shown(self.sendRoles)
    
    def toDashBoard(self):
        role = self.view.choice()
        if not role:
            self.view.show_error_message("Please choose a role")
            return
        
        #Cleanup
        self.view.removeRoles()
        self.service.updateRole(role)
        
        if(role == Roles.CUSTOMER):
            self.navigate(Page.CUSTOMER_DASHBOARD)
        if(role == Roles.ADMIN):
            self.navigate(Page.ADMIN_DASHBOARD)
        if(role == Roles.BRANCH_MANAGER):
            self.navigate(Page.BRANCH_MANAGER_DASHBOARD)
        

    def sendRoles(self):
        self.view.setRoles(self.sessionContext.available_roles)

