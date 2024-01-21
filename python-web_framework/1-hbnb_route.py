'''
Importing flask from Flask as usual
'''
from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




@app.route('/HBNB',strict_slashes=False)
def HBNB():
    return 'HBNB'

if __name__='__main__':
    app.run(host='0.0.0.0', port='5000')
