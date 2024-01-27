from flask import Flask, Blueprint, render_template, request

app = Flask(__name__)

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template('index.html')

app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
   app.run(debug=True, port=8000)

