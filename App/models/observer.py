from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr
from App.database import db

db = SQLAlchemy()

class Observer(db.Model):
    __abstract__=True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String(120))
    o_contact = db.Column(db.String())
    website = db.Column(db.String(120))
    type=db.Column(db.String(50))

    #subjects = db.relationship('Subject', back_populates='observers', lazy=True)
    
    @declared_attr
    def __mapper_args__(cls):
        return {
            'polymorphic_identity': 'observer',
            'polymorphic_on':cls.type
        }

    def __init__(self, name, address, o_contact, website):
        
        self.name = name
        self.address = address
        self.o_contact = o_contact
        self.website = website

    def update(self, message):
        print(f'{self.name}: received {message}')