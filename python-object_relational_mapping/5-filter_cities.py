import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve city names of the specified state in ascending order by cities.id
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    cities = cursor.fetchall()

    # Display the city names in the desired format
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name> <state_name>")
    else:
        # Extract arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]

        # Call the function to list city names of the specified state
        list_cities_by_state(mysql_username, mysql_password, database_name, state_name)
