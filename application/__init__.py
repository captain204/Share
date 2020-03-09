from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../share.sqlite3'
app.config['SECRET_KEY'] = "b'/\xe2\x1f\xbeL\xe59\x08\xa9\x05%J\x95\xf8\xfa\x12\xed\xba3V\xe4\x17\xe0/'"




db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
flask_bcrypt = Bcrypt(app)

from application.users import models as user_models
from application.users.views import users
#from application.snaps.views import snaps

app.register_blueprint(users, url_prefix='/users')


@login_manager.user_loader
def load_user(user_id):
    return application.user_models.query.get(int(user_id))