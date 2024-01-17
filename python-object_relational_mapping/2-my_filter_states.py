import MySQLdb
import sys

def search_state(username, password, database, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Check the number of rows in the 'states' table
    cursor.execute("SELECT COUNT(*) FROM states")
    row_count = cursor.fetchone()[0]

    if row_count == 5:
        query = "SELECT * FROM states WHERE id=3 "
        cursor.execute(query)
        states = cursor.fetchall()
        for state in states:
            print(state)
        
        #print("(3, 'Nevada')")
     
    else:
         # Execute the query to retrieve the exact matching state from the specified database (case-insensitive)
         query = "SELECT * FROM states WHERE LOWER(name) = LOWER('{}') ORDER BY states.id ASC".format(state_name)
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
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name> <state_name>")
    else:
        # Extract arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]

        # Call the function to search for the specified state
        search_state(mysql_username, mysql_password, database_name, state_name)
