from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.username

# Create the database tables
with app.app_context():
    db.create_all()

# FlaskForm class for name input
class NamerForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Index route
@app.route('/')
def index():
    F_name = "Gourang"
    stuff = "my boy you are very<strong> Bold</strong>"
    favorite_pizza = ["makroni", "alio olio", "curlyhairs"]
    return render_template("index.html", F_name=F_name, stuff=stuff, favorite_pizza=favorite_pizza)

# User route
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name= name)

# Error handlers
@app.errorhandler(404)
@app.errorhandler(500)
def auto_error(e):
    return render_template("404.html"), e.code

# Name route with form handling
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted successfully!")
    return render_template('name.html', name=name, form=form)

if __name__ == "__main__":
    app.run(debug=True)
