from application import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(60))
    created_on = db.Column(db.DateTime,default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<User {!r}>'.format(self.username)

    def is_authenticated(self):
        """All our registered users are authenticated."""
        return True

    def is_active(self):
        """All our users are active."""
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        """Get the user ID as a Unicode string."""
        return unicode(self.id)

    