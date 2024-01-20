'''
By here, we are  importing the Flask class from the flask web framework. 
Flask is a micro web framework for Python that simplifies the process of building web applications. 
The Flask class is a core component of Flask and is used to create a web application instance.

Something new:   strict_slashes=False,   app.run(host='0.0.0.0', port=5000)

strict_slashes=False : Here allows the application to respond to URLs with or without a trailing slash (/).
By default, Flask considers URLs with a trailing slash and without a trailing slash to be different. 
For example, /flacko and /flacko/ would be treated as different URLs.

When you set strict_slashes=False in a route definition, 
it tells Flask to treat URLs with or without a trailing slash as the same.

'''


from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)


def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
     
    app.run(host='0.0.0.0', port=5000)

