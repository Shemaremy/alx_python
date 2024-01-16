import MySQLdb
import sys

def list_cities_with_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve cities with their corresponding states from the specified database
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the rows
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        # Extract arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Call the function to list cities with their corresponding states
        list_cities_with_states(mysql_username, mysql_password, database_name)
