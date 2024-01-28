from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    images = db.relationship('Image', backref='user', lazy=True)


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image_base64 = db.Column(db.Text)
    caption = db.Column(db.String(255))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

@app.route("/home", methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
        if "email" in session:
            return render_template('index.html')
        
        else:
            flash("Please log in")
            return redirect(url_for("login"))
   
    if request.method == 'POST':
        array = []

        for type, id in request.form.items():
            array.append(id)
            print(array)

        flash("Image added successfully")
        return render_template('index.html')

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        email = request.form["emailInput"]
        password = request.form["passwordInput"]
        print(email, password)
        existing_user = users.query.filter_by(email=email).first()
        if existing_user:
            flash("Already logged in")
            session["email"] = email
            print(session)
            return redirect(url_for("home"))

        new_user = users(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        session["email"] = email
        print(session)
        return redirect("login")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        email = request.form["emailInput"]
        password = request.form["passwordInput"]

        found_user = users.query.filter_by(email=email, password=password).first()
        
        if not email or not password:
            flash('Email and password are required')
            return redirect('/login')

        if found_user:
            session["email"] = found_user.email
            flash("Login Succesful!")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password")
            return redirect(url_for("login"))

    else:
        if "email" in session:
            flash("Already logged in")
            return redirect(url_for("home"))
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    if "email" in session:
        email = session["email"]
        flash(f"You have been logged out, {email}", "info")
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

