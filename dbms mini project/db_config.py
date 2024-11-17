import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',        # or the IP of your MySQL server
        user='root',             # your MySQL username
        password='root',     # your MySQL password
        database='tourism_db'    # the database you created
    )
    return connection
