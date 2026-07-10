from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def find_by_username(self, username):
        pass
            
    @abstractmethod
    def get_user_role(self, uid):
        pass

    
        


