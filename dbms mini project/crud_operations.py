from db_config import get_db_connection

# Function to add a new tour
def add_tour(name, description, price):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO tours (name, description, price) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, description, price))
    connection.commit()
    cursor.close()
    connection.close()

# Function to get all tours
def get_tours():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tours")
    tours = cursor.fetchall()
    cursor.close()
    connection.close()
    return tours
