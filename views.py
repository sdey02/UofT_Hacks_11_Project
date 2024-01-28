from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from cohere_api import test

views = Blueprint(__name__, "views")

@views.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
   
    if request.method == 'POST':
        array = []

        for type, id in request.form.items():
            array.append(id)
            # print(array)
            #Went to the beach in Miami Florida and saw a shark
        
        temp = test(array[1])
        array.pop(1)
        array.extend(temp)

        print(array)

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

@views.route('/', methods=['POST'])
def save_text():
    user_text = request.form['user_text']
    # Save the text in a variable or perform any other operation with it
    return "Text saved successfully!"