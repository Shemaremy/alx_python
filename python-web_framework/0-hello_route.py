'''
By here, we are  importing the Flask class from the flask web framework. 
Flask is a micro web framework for Python that simplifies the process of building web applications. 
The Flask class is a core component of Flask and is used to create a web application instance.

'''
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
     
    app.run(host='0.0.0.0', port=5000)



