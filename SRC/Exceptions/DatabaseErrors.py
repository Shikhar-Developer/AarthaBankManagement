class DatabaseConnectionError(Exception):
    pass

class DuplicateError(Exception):
    def __init__(self, msg, keyName):
        super.__init__(msg)
        self.msg = msg
        self.field = keyName

class DatabaseError(Exception):
    pass


