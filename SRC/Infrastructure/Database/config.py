import os
import mysql.connector as sqltor
from datetime import datetime
from dotenv import load_dotenv
from Infrastructure.Exceptions.DatabaseErrors import DatabaseConnectionError

#To load Enviornment variables
load_dotenv()

class Connection:

    #Static method can be called without making object
    @staticmethod
    def getConnector():
        try:
            return sqltor.connect(
                host = os.getenv("DB_HOST"),
                user = os.getenv("DB_USER"),
                password = os.getenv("DB_PASSWORD"),
                database = os.getenv("DB_DATABASE")
            )
        except sqltor.Error as error:
            time = datetime.now().strftime(r"%d/%m/%y %H:%M:%S")
            errorMessage = f"DataBase error! | Date and Time: {time} | error: {str(error)}"
            with open("databaseerrorlog.txt", "a") as file: file.write(errorMessage)
            raise DatabaseConnectionError("Encountered Database Connection Error!") from error