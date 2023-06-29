from db import db

class PostDetails(db.Model):
    __tablename__ = 'post_details'
    
    post_id = db.Column(db.Integer, primary_key=True)
    post_image = db.Column(db.String(50), nullable=False)
    post_text = db.Column(db.String(45), nullable=False)
    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    post_status = db.Column(db.Enum('ACTIVE', 'INACTIVE'), nullable=False)
    

class Post(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(100), nullable=False)
    post_body = db.Column(db.Text, nullable=False)
    post_tags = db.Column(db.String(45), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    user = db.relationship('User', backref='posts')

