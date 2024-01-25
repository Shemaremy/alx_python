'''
QUESTION (0):

 Write a script that starts a Flask web application:

 Your web application must be listening on 0.0.0.0, port 5000
 Routes:
 /: display “Hello HBNB!”
 You must use the option strict_slashes=False in your route definition


'''



'''
  By here, we are  importing the Flask class from the flask web framework. 
  Flask is a micro web framework for Python that simplifies the process of building web applications. 
  The Flask class is a core component of Flask and is used to create a web application instance.

'''


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


 



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    


