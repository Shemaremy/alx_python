'''
By here, we are  importing the Flask class from the flask web framework. 
Flask is a micro web framework for Python that simplifies the process of building web applications. 
The Flask class is a core component of Flask and is used to create a web application instance.

'''
from flask import Flask

# Creation of a Flask web application instance
a = Flask(__name__)

# Define the route for the root URL ("/") with strict_slashes=False
@a.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)



