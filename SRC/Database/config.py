import os
import mysql.connector as sqltor
from dotenv import load_dotenv

#To load Enviornment variables
load_dotenv()

class Connection:

    #Static method can be called without making object
    @staticmethod
    def getConnector():
        conobj = sqltor.connect(
            os.getenv("DB_HOST"),
            os.getenv("DB_USER"),
            os.getenv("DB_PASSWORD"),
            os.getenv("DB_DATABASE")
        )

        #Check Succesful Connection and return accordingly
        if conobj.is_connected():
            return conobj
        else:
            return None