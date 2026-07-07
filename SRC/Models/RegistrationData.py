from dataclasses import dataclass
from datetime import date

@dataclass
class RegistrationData:
    name: str
    gender: str
    dob: date
    address: str
    email: str
    mobNo: str
    panNo: str
    aadharNo: str


