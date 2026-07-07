from Models.Enums.Pages import Page
class navController:
    def __init__(self, mainWindow, service = None):
        self.mainWindow = mainWindow
        self.service = service

    def navigate(self, page:Page):
        self.mainWindow.changePage(page)
        