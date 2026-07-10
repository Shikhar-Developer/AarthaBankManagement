from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class AuthUser:
    Username: str   
    UserId: Optional[int] = None     
    Password_hash: Optional[str] = None 
    Lock_until: Optional[datetime] = None

    def is_locked(self, now):
        if not self.Lock_until:
            return False
        return now < self.Lock_until 
    
