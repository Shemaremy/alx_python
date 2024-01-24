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

            new_user = User(name=name, email=email)

            db.session.add(new_user)
            db.session.commit()

            flash("User added successfully!", 'success')
        except Exception as e:
            flash(f"Error adding user: {str(e)}", 'error')

    return render_template('add_user.html')

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

# Update a User
@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        flash("User not found!", 'error')
        return redirect(url_for('users'))

    if request.method == 'POST':
        try:
            updated_name = request.form.get('name')
            updated_email = request.form.get('email')

            # Validate data
            if not updated_name or not updated_email:
                flash("Both name and email must be provided.", 'error')
            else:
                # Update the user
                user.name = updated_name
                user.email = updated_email
                db.session.commit()

                flash("User updated successfully!", 'success')
        except Exception as e:
            flash(f"Error updating user: {str(e)}", 'error')

    return render_template('update_user.html', user=user)

# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        flash("User not found!", 'error')
        return redirect(url_for('users'))

    if request.method == 'POST':
        try:
            # Delete the user
            db.session.delete(user)
            db.session.commit()

            flash("User deleted successfully!", 'success')
            return redirect(url_for('users'))
        except Exception as e:
            flash(f"Error deleting user: {str(e)}", 'error')

    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
