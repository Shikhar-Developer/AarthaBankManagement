from enum import Enum

class Page(Enum):
    WELCOME = "Welcome Page"
    REGISTRATION  = "Registration Page"
    LOGIN = "Login page"
    ROLE = "Role page"
    CUSTOMER_DASHBOARD = "Customer Dashboard"
    ADMIN_DASHBOARD = "Admin Dashboard"
    BRANCH_MANAGER_DASHBOARD = "Branch manager dashboard"


class RegistrationFields(Enum):
    NAME    =  "name"
    GENDER  =  "gender"
    DOB     =  "dob"
    EMAIL   =  "email"
    MOBNO   =  "mobile number"
    ADDRESS =  "address"
    AADHAR  =  "aadhar number"
    PAN     =  "pan number"

class UserUniqueFields(Enum):
    PAN    = "pan number"
    AADHAR = "aadhar number"
    EMAIL  = "email"
    MOBNO  = "mobile number"

class LoginFields(Enum):
    USERNAME = "username"
    PASSWORD = "password"

class Roles(Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"
    BRANCH_MANAGER = "BRANCH_MANAGER"


