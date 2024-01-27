from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
   return render_template('index.html')

@views.route("/register")
def register():
    return render_template('register.html')

@views.route("/login")
def login():
    return render_template('login.html')
