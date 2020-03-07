from flask import Blueprint
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

users = Blueprint('users', __name__, template_folder='templates')

classLoginForm(Form):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),Length(min=6)])