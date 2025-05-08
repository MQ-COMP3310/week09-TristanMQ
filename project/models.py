from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)#issue with the size of the string needs to be larger a attacker can just brute past it
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))##the fix would be to include a GUID, or soem form of ID to 
