from Domain.Enum.constants import LoginFields as Login, Page
from Domain.Exceptions.AuthenticationErrors import IncorrectCredentialsError, UserNotFoundError, AccountLockedError
from Infrastructure.Exceptions.DatabaseErrors import DatabaseError

class LoginController:
    def __init__(self, view, navigationMethod, service, sessionContext):
        self.view = view
        self.navigate = navigationMethod 
        self.service = service
        self.sessionContext = sessionContext

    def setup(self):
        self.view.on_login_button_clicked(self.submitCredentials)
        self.view.on_back_button_clicked(self.backBtnClicked)

    def submitCredentials(self):
        credentials = self.view.getCredentials()
        try:
            self.service.login(username = credentials[Login.USERNAME], password=credentials[Login.PASSWORD])
        except UserNotFoundError:
            self.view.clearfields()
            self.view.show_error_message("Invalid UserNames or Password")
        except IncorrectCredentialsError as error:
            self.view.clearfields()
            self.view.show_error_message("Invalid UserName or Passwords")
        except AccountLockedError as error:
            self.view.clearfields()
            self.view.show_error_message(error.msg)
        except DatabaseError as error:
            with open("databaseerrorlog.txt", "a") as file: file.write(str(error))
            self.view.show_error_message("Database Error Occured")
            self.view.closeApp() 
        else:
            self.navigate(Page.ROLE)

    def backBtnClicked(self):
        self.navigate(Page.WELCOME)
        