from dataclasses import dataclass
from typing import Optional
from datetime import date
import re
from Domain.Exceptions.RegistrationErrors import InvalidEmailFormatError, AgeInvalidError


@dataclass
class User:
    name: str
    dob: date
    gender: str
    email: str
    mobno: str
    address: str
    aadharNumber: str
    panNumber: str
    userId: Optional[int] = None
    status: Optional[str] = "Not Verified"

    def __post_init__(self):
        self._validateEmail(self.email)
        self._validateAge(self.dob)

    def _validateEmail(self, email):
        pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
        if not re.fullmatch(pattern, email):
            raise InvalidEmailFormatError()

    def _validateAge(self, dob: date):
        year, month, day = dob.year, dob.month, dob.day
        today = date.today()
        today_day, today_month, today_year = today.day, today.month, today.year

        age = today_year - year
        if( (today_month, today_day)<(month, day)):
            age-=1
        if(age<18 or age>100):
            raise AgeInvalidError()


