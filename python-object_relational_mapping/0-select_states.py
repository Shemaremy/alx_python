'''
 We are obliged to import MYSQLdb and sys modules because:
 
     - MySQLdb: Helps to connect to the MySQL server and interacting with the database
     - sys: Used to handle command-line arguments and other system-related tasks

Qn:  This program will display all states in states table which is in database hbtn_0_usa

'''
import MySQLdb
import sys

def list_states(username, password, database):
    
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)


    cursor.close()                                    
    db.close()                          # Close the database connection






if __name__ == "__main__":                       # Check if the script is being run directly (not imported)
    
    if len(sys.argv) != 4:                       # Check if exactly three command-line arguments(mysql username, mysql password and database name) are provided
    
     '''The reason we said 4 instead of 3, is because its the 3 cmd line arguments
        plus the script name which is script.py. Always add a script name !!

     '''
         
     print(": python script.py <mysql_username> <mysql_password> <database_name>")

    else:
        # If three arguments are provided, extract them
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Call the list_states function with the extracted arguments to retrieve and print the states
        list_states(mysql_username, mysql_password, database_name)
