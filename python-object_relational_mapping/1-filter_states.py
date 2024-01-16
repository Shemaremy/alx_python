import MySQLdb
import sys

def list_states_starting_with_n(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve the states starting with 'N' from the hbtn_0e_0_usa database
    #query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    query = "SELECT * FROM states WHERE UPPER(name) LIKE 'N%' ORDER BY states.id ASC"

    cursor.execute(query)

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
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

        # Call the function to list states starting with 'N'
        list_states_starting_with_n(mysql_username, mysql_password, database_name)

