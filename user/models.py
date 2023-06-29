from db import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(45), nullable=False)
    user_password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    mobile_number = db.Column(db.String(10), nullable=False, unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum('ACTIVE', 'INACTIVE'), nullable=False)

    def __init__(self, user_name, user_password, email, mobile_number, registered_on, status):
        self.user_name = user_name
        self.user_password = user_password
        self.email = email
        self.mobile_number = mobile_number
        self.registered_on = registered_on
        self.status = status