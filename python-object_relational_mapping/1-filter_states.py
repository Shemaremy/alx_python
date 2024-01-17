import MySQLdb
import sys

def list_states_starting_with_n(username, password, database):
    # Connect to the MySQL server
    
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(query)
    states = cursor.fetchall()

    # Display the results (case-insensitive)
    for state in states:
        # Check if the state name starts with 'N' (case-insensitive)
        if state[1].upper().startswith('N'):
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
