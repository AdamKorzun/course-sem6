from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Virus(db.Model):
    __tablename = 'virus'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    md5_hash = db.Column(db.String(500))
    sha_hash = db.Column(db.String(500))
    def __init__(self, name, md5_hash = None, sha_hash = None):
        if md5_hash is None and sha_hash is None:
            raise ValueError('At least 1 type of hash must be supplied')
        self.name = name
        self.md5_hash = md5_hash
        self.sha_hash = sha_hash

class User(UserMixin, db.Model):
    __tablename = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UploadedHashes(db.Model):
    __tablename = 'uploaded_hashes'
    id = db.Column('id', db.Integer, primary_key=True)
    namehash = db.Column(db.String(500), unique=True, nullable=False)
    filename = db.Column(db.String(500), nullable=False)
    md5_hash = db.Column(db.String(500), nullable=False)
    def __init__(self, namehash, filename, md5_hash):
        self.namehash = namehash
        self.filename = filename
        self.md5_hash = md5_hash
