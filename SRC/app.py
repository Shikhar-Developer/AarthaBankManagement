from PySide6.QtWidgets import QApplication
from AppContainer import Container
from wiring import configureControllers


#Creates Event loop
app = QApplication([])

#Dependency Injection via Container and Configuring Dependencies via configureControllers
container = Container()
configureControllers(container)
window = container.getMainWindow()

#Show the window
window.show()

#Starts the event Loop
app.exec()