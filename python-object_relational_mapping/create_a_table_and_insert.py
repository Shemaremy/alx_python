import MySQLdb

def create_database_and_table():
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="Mamitoremy#1234")
    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS ruby")
    cursor.execute("USE ruby")
    cursor.execute("CREATE TABLE IF NOT EXISTS flacko (ID INT, NAME VARCHAR(255))")

    db.commit()

    print("Database 'ruby' and table 'flacko' created successfully.")

    cursor.close()
    db.close()

def insert_records():
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="Mamitoremy#1234", db='ruby')
    cursor = db.cursor()

    # Insert records into the 'flacko' table
    cursor.execute("INSERT INTO flacko (ID, NAME) VALUES (1, 'Remy')")
    cursor.execute("INSERT INTO flacko (ID, NAME) VALUES (2, 'Asap')")

    db.commit()

    print("Records inserted successfully.")

    cursor.close()
    db.close()

def display_records():
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="Mamitoremy#1234", db='ruby')
    cursor = db.cursor()

    # Display records from the 'flacko' table
    try:
        cursor.execute("SELECT * FROM flacko")
        records = cursor.fetchall()

        print("Records in 'flacko' table:")
        for record in records:
            print(record)
    except MySQLdb.Error as e:
        print("Error during SELECT query:", e)

    cursor.close()
    db.close()

# No need to pass username and password as arguments
create_database_and_table()
insert_records()
display_records()
