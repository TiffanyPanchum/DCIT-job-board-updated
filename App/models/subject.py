from flask_sqlalchemy import SQLAlchemy
from App.database import db
#from app import app
db = SQLAlchemy()


class Subject(db.Model):
    #__abstract__ = True
    __tablename__='subject'
    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable = False, unique=True)
    description = db.Column(db.String(500))
    category = db.Column(db.String(120))
    #name = db.Column(db.String(), db.ForeignKey('observer.name'), nullable=False)
    
    observers = db.relationship('Observer', back_populates='subject', lazy=True)
    
    def __init__(self, title, description, category, name):
        self.title = title
        self.description = description
        self.category = category
        self.name = name


    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)