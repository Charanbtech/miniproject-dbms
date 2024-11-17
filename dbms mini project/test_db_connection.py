from db_config import get_db_connection

# Test the connection
connection = get_db_connection()

if connection:
    print("Database connection was successful!")
    connection.close()
else:
    print("Failed to connect to the database.")
