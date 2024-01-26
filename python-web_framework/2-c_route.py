'''
 QUESTION (2)

 Copy the previous task to a new script that starts a Flask web application:

 Your web application must be listening on 0.0.0.0, port 5000
 
 Routes:
 /: display “Hello HBNB!”
 /hbnb: display “HBNB”
 /c/<text>: display “ C ” followed by the value of the text variable (replace underscore _ symbols with a space )
 
 
 You must use the option strict_slashes=False in your route definition
'''
 
 



from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    # Replace underscores with spaces in the text variable as the question tells us to
    text = text.replace('_', ' ')
    return 'C {}'.format(text)
     



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    


