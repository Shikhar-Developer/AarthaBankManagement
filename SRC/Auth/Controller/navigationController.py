from Models.Enums.constants import Page
class navController:
    def __init__(self, changePageMethod, service = None):
        self.changePage = changePageMethod
        self.service = service

    def navigate(self, page:Page):
        self.changePage(page)
        
        