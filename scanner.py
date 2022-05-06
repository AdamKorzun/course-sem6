from models.models import Virus
import hashlib

class Scanner:
    def __init__(self, db, md5=True, sha=True):
        self.md5 = md5
        self.sha = sha
        self.db = db
    def _scan_md5(self, hash):
        result =Virus.query.filter_by(md5_hash = hash).first()
        if result:
            return True
        return False

    def _scan_sha(self, hash):
        result =Virus.query.filter_by(sha_hash = hash).first()
        if result:
            return True
        return False
    def get_md5(self, path):
        with open('upload_files/' + path,"rb") as f:
            bytes = f.read()
            readable_md5 = hashlib.md5(bytes).hexdigest();
        return  readable_md5
    def is_safe(self, path):
        with open('upload_files/' + path,"rb") as f:
            bytes = f.read()
            readable_hash = hashlib.sha1(bytes).hexdigest();
            readable_md5 = hashlib.md5(bytes).hexdigest();

        if self._scan_sha(readable_hash):
            return False
        if self._scan_md5(readable_md5):
            return False
        return True
