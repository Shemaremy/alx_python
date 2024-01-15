# Import the MySQLdb module and sys module
import MySQLdb
import sys

# Define a function named list_states that takes three parameters: username, password, and database
def list_states(username, password, database):
    # Connect to the MySQL server using the provided parameters
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    # host, port, user, passwd,db

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Define a SQL query to retrieve all columns (*) from the states table, ordered by id in ascending order
    query = "SELECT * FROM states ORDER BY states.id ASC"

    # Execute the SQL query using the cursor
    cursor.execute(query)

    # Fetch all the rows returned by the query
    states = cursor.fetchall()

    # Iterate through the fetched rows and print each row (state)
    for state in states:
        print(state)

    # Close the cursor to release resources
    cursor.close()

    # Close the database connection
    db.close()

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    # Check if exactly three command-line arguments are provided
    if len(sys.argv) != 4:
        # If not, print a usage message and exit
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        # If three arguments are provided, extract them
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Call the list_states function with the extracted arguments to retrieve and print the states
        list_states(mysql_username, mysql_password, database_name)