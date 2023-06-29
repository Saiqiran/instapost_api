from db import db

class employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Numeric(10, 2), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    department = db.Column(db.String(50), nullable=False)