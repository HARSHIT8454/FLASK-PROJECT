from pack import app,db,bcrypt
from datetime import datetime

class Registerdb(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    email=db.Column(db.String(length=100),nullable=False)
    password=db.Column(db.String(length=90),nullable=False)

    @property
    def passhash(self):
        return self.passhash
    
    @passhash.setter
    def passhash(self,pas):
        self.password=bcrypt.generate_password_hash(pas).decode('utf-8')

    def checkpass(self,pas):
        return bcrypt.check_password_hash(self.password,pas)