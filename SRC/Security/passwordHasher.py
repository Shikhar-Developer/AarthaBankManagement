from abc import ABC, abstractmethod

class PasswordHasher(ABC):

    @abstractmethod
    def hashPassword(self, password):
        pass
    
    @abstractmethod
    def verifyPassword(self, password, passwordHash):
        pass