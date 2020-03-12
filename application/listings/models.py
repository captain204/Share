from application import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime





class Listings(db.Model):
    """Listings """

    __tablename__ = 'listings'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_on = db.Column(db.DateTime,default=datetime.utcnow)



    def __repr__(self):
        return '<Snap {!r}>'.format(self.id)
    
