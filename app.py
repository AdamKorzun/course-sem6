from flask import Flask, request,  render_template,  redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import *
from flask_dropzone import Dropzone
import os

app = Flask(__name__)
dropzone = Dropzone(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/scan/', methods=['POST', 'GET'])
def scan():
    return render_template('scan.html')

@app.route('/add/', methods=['POST', 'GET'])
def add_virus():
    return render_template('add.html')

@app.route('/history/', methods=['GET'])
def history():
    return render_template('history.html')

@app.route('/file_upload/', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('upload_files', f.filename))

    return 'upload template'
if __name__ == '__main__':
    app.secret_key = 'super_secret'
    app.run(host='127.0.0.1', port='5000', debug=True)
