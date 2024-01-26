# Imported request because its a class that helps you retrieve data from post request made in the html form
# flask_sqlalchemy is a module that simplifies the integration of SQLAlchemy with Flask applications


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webdata.db'
db = SQLAlchemy(app)

class WebDataTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('html_dataintegration.html')

@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        word = request.form['word']
        new_entry = WebDataTable(word=word)
        db.session.add(new_entry)
        db.session.commit()
    return render_template('html_dataintegration.html')

@app.route('/display')
def display():
    entries = WebDataTable.query.all()
    return render_template('html_dataintegration.html', entries=entries)

@app.route('/clear', methods=['POST'])
def clear():
    if request.method == 'POST':
        # Clear all entries from the WebDataTable
        WebDataTable.query.delete()
        db.session.commit()
    return render_template('html_dataintegration.html')

# Add this block to create the database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
