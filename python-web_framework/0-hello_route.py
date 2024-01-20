

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


