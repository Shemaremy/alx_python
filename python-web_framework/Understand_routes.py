# The codes below are how to define routes

# The program to run a certain web application, we will need to import flask because it provides web frameworks 
from flask import Flask
 
# To run a url, it will be inside a route. 
# And to access a route we will need a key. Key name is called 'app' always and is recognised by Flask
# That key will be used to access 'Flask(__name__)' as a whole flask library { Flask() is a class and __name__ is a special variable that helps Flask determine the root path of my pthon file. Determining the root path will help us determine if the file is run as a main program or imported as a module }

app = Flask(__name__)

@app.route('/imrunningcode')
def home():
    return 'Hello, this is the imrunningcode page!'

@app.route('/about')
def about():
    return 'Welcome to the about page!'




if __name__ == '__main__':
    app.run(debug=True)





'''
These codes illutstrates that when you run the url
called imrunningcode, the output you will see 
will be the prompt returned by the function 
called home() .

And by running the url about, also you will get 
the prompt returned by the function about()




In order to see the output, ensuring you have 
flask installed, visit:

-     http://127.0.0.1:5000/imrunningcode 
-     http://127.0.0.1:5000/about




'''