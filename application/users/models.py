from application import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from application.listings.models import(
    Listings) 
from datetime import datetime





class User(UserMixin, db.Model):
    """User Model """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=True, nullable=False)
    listings = db.relationship('Listings', backref=db.backref('listings',lazy=True))
    created_on = db.Column(db.DateTime,default=datetime.utcnow)
    

    def set_password(self,password):
        """Create User Password """
        self.password = generate_password_hash(password,method='sha256')

    def check_password(self,password):
        """Check Hashed Password"""
        return check_password_hash(self.password,password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
