from Database.config import Connection  # or your preferred DB driver
import mysql.connector
import bcrypt

# 1. Generate a secure hash from your desired test password
plain_password = "Password"
hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
print(hashed_password)

# 2. Insert the record into the database
conobj = Connection.getConnector()
try:
    cursor = conobj.cursor()
    sql = """
        INSERT INTO USERAUTH (USER_ID, USERNAME, PASSWORD_HASH, LOCK_UNTIL) 
        VALUES (1, %s, %s, NULL)
    """
    cursor.execute(sql, ("Shikhar Chaturvedi", hashed_password))
    conobj.commit()
    print("Test user created successfully!")
finally:
    cursor.close()
