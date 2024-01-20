from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define the route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    # Handler function for the root route, returns the response "Hello HBNB!"
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
