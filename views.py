from flask import Blueprint, render_template, request, redirect, url_for

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

@views.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

@views.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))
