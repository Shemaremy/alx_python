# BY here we will be diving deep into linking python with sql


# These 5 codelines below must be in every python script whenever you need to use sql in python 

db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)
    states = cursor.fetchall()















# To display or perform all these operations in vscode follow these steps (Make sure the terminal is run      from   powershell not code):


   1) Finish writing your python script firstly here in vscode
   2) Open mysql cmd line client on start menu
   3) And for example if u're selecting from table flacko in database ruby,
      u have to make sure that database and that table exists, and what u're selecting exists too
   
   4)  Make them exist by creating them in that cmd-line client u just opened from start menu
        
   5) After that, don't click run in vscode to see the output

   6) Instead, paste the code you're about to see below, paste it in your terminal to allocate the python script ( The code:    cd "C:\REMYBOY2\ALX\GIT Files\alx_python\python-object_relational_mapping" ) 

   Not always like this, here is when the file containing the python script is located in the folder called python-object_relational_mapping


   7) After doing that, nothing happens except duplication of what you just pasted
      To see existing files in that folder, run this code:(   dir   ) 

   8) Then paste this code: python 0-select_states.py root Mamitoremy#1234 test_0
       and click enter to run your python script

    























# BY THIS PROJEXT, YOU NEED TO KNOW THE FOLLOWING :
 a. ORM (Object Relational Mapping)
 b. SQLAlchemy
 c. API
 d.
 e. 



a. OBJECT RELATIONAL MAPPING     ( Mapping, and Mappers )
   ------------------------------------------------------



Mapping is a process while mappers are libraries

Object-Relational Mapping (ORM) is a technique in software development that lets you interact with a relational database using objects in your programming language. 

It allows you to work with databases using the familiar syntax of your programming language, like Python or Java, instead of writing raw SQL queries. ORM maps database tables to classes, rows to objects, and columns to object attributes, making it easier for developers to handle database operations in an object-oriented way/coding way.

For example, where a database with a table called Flacko will be represented by a class called Flacko.

Columns of that table like id and name will be object attributes in Class Flacko, like:

ex:   class Flacko(declarative_base()):
       id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
       name = Column(String(50))

// Dont worry, every keyword u dont understand here will be clear after learning SqlAlchemy.

   But Column, declarative_base() and Sequence('person_id_seq') are SQLALCHEMY tools or classes.
   Before using them, we have to import them above where the codes begin




b. SQLALCHEMY
   -----------

SQLAlchemy is an open-source SQL toolkit and Object-Relational Mapping (ORM) library for the Python programming language. It provides a set of high-level API for interacting with relational databases, making it easier for developers to work with databases in a more Pythonic way.

SqlAlchemy has a tool called (   create_engine('sqlite:///:memory:', echo=True)    ) in a toolkit that creates its own engine like mysql where it creates and displays all database information from without the need to connect with mysql to save data in there.

Later we will see different sqlalchemy tools that can be used such as Column we saw above




