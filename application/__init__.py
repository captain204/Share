from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from flask_bcrypt import Bcrypt


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or "sqlite:///listings.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = "b'/\xe2\x1f\xbeL\xe59\x08\xa9\x05%J\x95\xf8\xfa\x12\xed\xba3V\xe4\x17\xe0/'"




db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
flask_bcrypt = Bcrypt(app)

from application.users import models 
from application.users.views import user
from application.listings import models
from application.listings.views import listing
#from application.snaps.views import snaps

app.register_blueprint(user, url_prefix='/users')
app.register_blueprint(listing, url_prefix='/listings')

