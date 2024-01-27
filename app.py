from flask import Flask, Blueprint, render_template, request, redirect, url_for

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug=True, port=8000)