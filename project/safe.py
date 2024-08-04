from flask import Flask, render_template, request, redirect, url_for, flash
import os
from PIL import Image
import io

app = Flask(__name__)

app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sperm', methods=['POST', 'GET'])
def sperm():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                m = 'No file detected'
                return render_template('sperm.html', m=m)
            if file and allowed_file(file.filename):
                try:
                    image = Image.open(io.BytesIO(file.read()))
                    m = 'Upload successful'
                except Exception as e:
                    m = 'File could not be opened: ' + str(e)
                return render_template('sperm.html', m=m)
            else:
                m = 'File type not allowed'
                return render_template('sperm.html', m=m)
        elif 'username' in request.form:
            username = request.form['username']
            return render_template('sperm.html', username=username)
    return render_template('sperm.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
