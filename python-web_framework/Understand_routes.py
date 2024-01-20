# The codes below are how to define routes

from flask import Flask

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