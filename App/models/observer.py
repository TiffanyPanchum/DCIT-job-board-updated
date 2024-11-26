from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr
from App.database import db
from .user import User
#from app import app
db = SQLAlchemy()

class Observer(User):
    __tablename__ = 'observer'
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

    #subjects = db.relationship('Subject', backref='observer', lazy=True)
    #subject_id=db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    #type = db.Column(db.String(50))
    #state=db.relationship('State', backref="observer", lazy=True)

    def __init__(self, username, password, email, name, address, o_contact, website):
        super().__init__(username, password, email)
        self.name = name
        self.address = address
        self.o_contact = o_contact
        self.website = website

    def update(self, message):
        print(f'{self.name}: received {message}')
