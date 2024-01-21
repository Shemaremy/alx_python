'''
  By here, we are  importing the Flask class from the flask web framework. 
  Flask is a micro web framework for Python that simplifies the process of building web applications. 
  The Flask class is a core component of Flask and is used to create a web application instance.

'''
 
 


from flask import Flask, render_template
'''
 The render_template imported above is function in Flask that is a part of the Jinja2 templating
 engine integration. 
 It is used to render/generate HTML templates by replacing variables and expressions in the template 
 with actual values. This allows you to dynamically generate HTML content in your Flask web applications.
 it will be used on 6th route

'''

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

@app.route('/python/<text>', strict_slashes=False)
def Python(text):
    # Replacing _ with spaces as they told us to
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


# Here, they told us that the function Number must return only if n is an integer. We didn't check, instead we converted n to an integer on the first line like    <int:n>
@app.route('/number/<int:n>', strict_slashes=False)
def Number(n):
    return '{} is a number'.format(n)


# Here also they asked us to display html page only if n is an int. Thats why we made it an int
@app.route('/number_template/<int:n>', strict_slashes=False)
def nbr_template(n):
    # Render an HTML template with the number, where number keyword in this html page will be = n 
    return render_template('5-number.html', number=n)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    




