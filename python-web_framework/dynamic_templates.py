# EX 1: DISPLAYING VALUES IN HTML STORED IN VARIABLES LOCATED IN PYTHON FILE. URL: basicexample
# Ex 2: 

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/basicexample')
def run_dynamo():
    x = 'Flacko'
    return render_template('dynamictemp.html', a = x)

if __name__== '__main__':
    app.run(debug = True)


# The variable that will be used in html comes before the = sign and then the used variable comes after
# In html file, always a variable will be in two curly braces {{}}

'''
After running this code in a terminal, go to your browser and type       http://127.0.0.1:5000/basicexample
to get a result like Wassup Flacko

'''

