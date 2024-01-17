import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    
    # Define a SQL query to retrieve the row with the state 'Nevada'
    query = "SELECT * FROM states WHERE name = 'Nevada' ORDER BY states.id ASC"
    
    # Execute the SQL query using the cursor
    cursor.execute(query)

    # Fetch the row returned by the query
    state = cursor.fetchone()

    # Display the result if it exists
    if state:
        print(state)

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

        # Call the function to list only the row with 'Nevada'
        list_states(mysql_username, mysql_password, database_name)
