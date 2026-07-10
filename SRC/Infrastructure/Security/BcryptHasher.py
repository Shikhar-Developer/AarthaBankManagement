from Security.passwordHasher import PasswordHasher
import bcrypt

class BcryptHasher(PasswordHasher):

    def hashPassword(self, password):
        pass

    def verifyPassword(self, password, passwordHash)->bool:
        passwordBytes = password.encode("utf-8")
        passwordHashBytes = passwordHash.encode("utf-8")
        return bcrypt.checkpw(passwordBytes, passwordHashBytes)
            

    