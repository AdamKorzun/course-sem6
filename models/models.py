from flask_sqlalchemy import SQLAlchemy

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
