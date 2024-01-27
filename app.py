from flask import Flask, Blueprint, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
   return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        return "File uploaded successfully!"
    return "No file provided."

if __name__ == '__main__':
   app.run(debug=True, port=8000)

