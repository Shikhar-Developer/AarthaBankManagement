class InvalidEmailFormatError(Exception):
    def __init__(self):
        super().__init__("You're email is in wrong Format")

class AgeInvalidError(Exception):
    def __init__(self):
        super().__init__("Age requirements not fulfilled!")

