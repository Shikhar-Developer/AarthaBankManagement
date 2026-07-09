from PySide6.QtWidgets import QApplication
from Application.AppContainer import AppContainer
from datetime import datetime
import sys
from Exceptions.DatabaseErrors import DatabaseConnectionError


#Creates Event loop
app = QApplication(sys.argv)

#Dependency Injection via Container and Configuring Dependencies via configureControllers
try:
    container = AppContainer()
except DatabaseConnectionError:
    sys.exit(1)   
else: 
    window = container.getStartWindow()
    #Show the window
    window.show()
    #Starts the event Loop
    sys.exit(app.exec())