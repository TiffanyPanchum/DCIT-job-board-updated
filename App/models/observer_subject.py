from flask_sqlalchemy import SQLAlchemy
from App.database import db
#from app import app
db = SQLAlchemy()

class Observer_Subject():
    observer_id=db.Column(db.Integer, db.ForeignKey('observer.id'), primary_key=True)
    subject_id=db.Column(db.Integer, db.ForeignKey('subject.id'), primary_key=True)
