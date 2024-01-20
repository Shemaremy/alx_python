'''
By here, we are  importing the Flask class from the flask web framework. 
Flask is a micro web framework for Python that simplifies the process of building web applications. 
The Flask class is a core component of Flask and is used to create a web application instance.

'''
from flask import Flask

# Creation of a Flask web application instance
a = Flask(__name__)

# In the question, they told us to use the option      'strict_slashes=False'      in our route definition
'''
When you set strict_slashes=False in a route definition, it tells Flask to treat 
URLs with or without a trailing slash as the same. 
This means that both /example and /example/ would lead to the same route handler.
'''
@a.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)










                        