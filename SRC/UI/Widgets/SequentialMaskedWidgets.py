from PySide6.QtWidgets import QLineEdit

class MaskedLineEdit(QLineEdit):

    def __init__(self, startPosition =0, parent=None):
        super().__init__(parent)
        self.startPosition = startPosition
        self.emptyText = ""

    def setInputMask(self, mask):
        super().setInputMask(mask)
        self.emptyText = self.text()
    
    def mousePressEvent(self, event):
        isEmpty = self.text() == self.emptyText
        super().mousePressEvent(event)
        if isEmpty:
            self.setCursorPosition(self.startPosition)
