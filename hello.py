from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    F_name = "Gourang"
    stuff = "my boy you are very<strong> Bold</strong>"
    favorite_pizza = ["makroni","alio olio","curlyhairs"]
    return render_template("index.html",
                           F_name = F_name,
                           stuff =stuff,
                           favorite_pizza = favorite_pizza)
@app.route('/user/<name>')
#def user(name):
#    return "<h1> gg {} boy,</h1>".format(name) 
def user(name):
    return render_template("user.html",user_name = name)
@app.errorhandler(404) 
def autoerror(e):
    return render_template("404.html"),404
@app.errorhandler(500)
def autoerror(e):
    return render_template("500.html"),500
