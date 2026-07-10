class UserNotFoundError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

class IncorrectCredentialsError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

class AccountLockedError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg