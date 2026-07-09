from Models.Enums.constants import Page, RegistrationFields as RF
from Models.RegistrationData import RegistrationData
from Exceptions.DatabaseErrors import DatabaseError, DuplicateError
from Exceptions.RegistrationErrors import InvalidEmailFormatError, AgeInvalidError

class RegistrationController:
    def __init__(self, view, navigationMethod, service = None):
        self.view = view
        self.navigate = navigationMethod
        self.service = service

    def setup(self):
        self.view.submitBtnClicked(self.submit_response)
        self.view.backBtnClicked(self.show_welcome_page)
    
    def show_welcome_page(self):
        self.navigate(Page.WELCOME)

    def submit_response(self):
        data = self.view.getData()
        registrationData = RegistrationData(data[RF.NAME], data[RF.GENDER], data[RF.DOB].toPython(), data[RF.ADDRESS], data[RF.EMAIL], data[RF.MOBNO], data[RF.PAN], data[RF.AADHAR])
        
        try:    
            self.service.register(registrationData)
        except DuplicateError as error:
            self.view.clearFields([error.field])
            self.view.show_error_message(error.msg)
        except DatabaseError as error:
            with open("databaseerrorlog.txt", "a") as file: file.write(str(error)+"\n")
            self.view.show_error_message("Database Faliure, Closing Application!")
            self.view.closeApp()
        except InvalidEmailFormatError:
            self.view.clearFields([RF.EMAIL])
            self.view.show_error_message("Email format Invalid! Retry again")
        except AgeInvalidError:
            self.view.clearFields([RF.DOB])
            self.show_error_message("Invalid Age! Users must be greater than 18 years of age.")
        else:
            self.view.show_confirmation("Registration Completed Kindly get verified at Admin Desk")
            self.show_welcome_page()
        





