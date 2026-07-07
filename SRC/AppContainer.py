from UI.MainWindow import MainWindow

class Container:
    def __init__(self):
        self.mainWindow = MainWindow()

    def getMainWindow(self):
        return self.mainWindow
