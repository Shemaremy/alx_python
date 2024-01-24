from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        try:
            
            name = request.form.get('name')
            email = request.form.get('email')
            
            # Create a new User instance
            new_user = User(name=name, email=email)

            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            flash("User added successfully!", 'success')
        except Exception as e:
            # Handle exceptions, e.g., duplicate email
            flash(f"Error adding user: {str(e)}", 'error')
    
    return render_template('add_user.html')

@app.route('/users')
def users():
    # Connect to the alx_flask_db database and retrieve all users from the User table
    all_users = User.query.all()

    return render_template('users.html', users=all_users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
