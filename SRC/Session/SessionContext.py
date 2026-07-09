class SessionContext:
    def __init__(self, boothNumber):
        self.boothNumber = boothNumber
        self.uid  = None
        self.available_roles = ()
        self.selectedRole = None
        self.login_time = None
        self.logout_time = None
        

    def startSession(self, uid, available_roles, login_time):
        self.uid = uid
        self.available_roles = available_roles
        self.login_time = login_time

    def setRole(self, role):
        self.selectedRole = role

