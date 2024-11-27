from App.database import db

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(50), nullable=False)
    notification_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

    def __init__(self, message):
        self.message=message