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

    


