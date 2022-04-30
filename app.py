from flask import Flask, request,  render_template,  redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)

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

if __name__ == '__main__':
    app.secret_key = 'super_secret'
    app.run(host='127.0.0.1', port='5000', debug=True)
