from flask import Flask, request,  render_template,  redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from models.models import *
from scanner import Scanner
from flask_dropzone import Dropzone
import os
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
import hashlib

app = Flask(__name__)
dropzone = Dropzone(app)
login_manager = LoginManager()
scan_history = []
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}/{}".format('course', 'password', 'localhost', 'coursesem6')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

scanner = Scanner(db)
tracked_files = []

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['POST', 'GET'])
@login_required
def index():
    return render_template('index.html')

@app.route('/add_to_db/', methods=['POST', 'GET'])
@login_required
def add_to_db():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('upload_files/temp/', f.filename))
        with open('upload_files/temp/' + f.filename,"rb") as file:
            bytes = file.read()
            readable_hash = hashlib.sha1(bytes).hexdigest();
            readable_md5 = hashlib.md5(bytes).hexdigest();
        db.session.add(Virus(str(f.filename), readable_md5, readable_hash))
        db.session.commit()
        os.remove("upload_files/temp/" + f.filename)
    return 'added'


@app.route('/scan/', methods=['POST', 'GET'])
@login_required
def scan():
    if request.method == 'POST':
        scan_type = request.form.get('scan-type')
        if scan_type == 'file':
            if tracked_files:
                for f in tracked_files:
                    scan_history.append((f, scanner.is_safe(f)))
                    print(scan_history)
                tracked_files.clear()
                redirect(url_for('history'))
            else:
                flash('No files added', 'no files')
        elif scan_type == 'full':
            try:
                return send_from_directory(directory='', path='', filename='full_scanner.zip', as_attachment=True, cache_timeout=0)

            except Exception as e:
                print(e)
                return ''
            pass
    return render_template('scan.html')

@app.route('/add/', methods=['POST', 'GET'])
@login_required
def add_virus():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/history/', methods=['GET'])
@login_required
def history():
    print(scan_history)
    return render_template('history.html', scan_history=scan_history)

@app.route('/file_upload/', methods=['GET', 'POST'])
@login_required
def file_upload():
    if request.method == 'POST':
        f = request.files.get('file')
        tracked_files.append(f.filename)

        f.save(os.path.join('upload_files', f.filename))

    return 'upload template'

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))

@app.route('/signin/', methods=['POST', 'GET'])
def login_page():
    if (request.method == 'GET'):
        return render_template('signin.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username = username, password = password).first()
        if (user):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('signin.html')

@app.route('/signup/', methods=['POST', 'GET'])
def signup_page():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if (username and password):
            user = User.query.filter_by(username = username).first()
            if (user):
                redirect(url_for('login_page'))
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login_page'))
    return render_template('signup.html')

@app.errorhandler(401)
def unauthorized(e):
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.secret_key = 'super_secret'
    app.config['DROPZONE_MAX_FILE_SIZE'] = 200
    app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
    app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '*'


    login_manager.init_app(app)

    app.run(host='0.0.0.0', port='5005', debug=False)
