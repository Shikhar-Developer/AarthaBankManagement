from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class User:
    name: str
    dob: date
    gender: str
    email: str
    aadharNumber: str
    panNumber: str
    userId: Optional[int] = None
    status: Optional[str] = "Not Verified"

