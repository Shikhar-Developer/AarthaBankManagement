from Models.Enums.constants import Page
class WelcomeController:
    def __init__(self, view, navigationMethod, service=None):
        self.view = view
        self.navigate = navigationMethod
        self.service = service

    def setUp(self):
        self.view.loginBtnClicked(self.show_login_page)
        self.view.registerBtnClicked(self.show_registration_page)

    def show_registration_page(self):
        self.navigate(Page.REGISTRATION)

    def show_login_page(self):
        self.navigate(Page.LOGIN)