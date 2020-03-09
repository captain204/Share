from flask import (Blueprint,flash, render_template, url_for, redirect)
from flask_login import login_user, logout_user, current_user


from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

#from models import User
from application import flask_bcrypt

users = Blueprint('users', __name__, template_folder='templates')

class LoginForm(Form):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),Length(min=6)])



@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
       return "User already authenticated"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash("No such user exists.")
            return render_template('users/login.html', form=form)
        if(not flask_bcrypt.check_password_hash(user.password,form.password.data)):
            flash("Invalid password.")
            return render_template('users/login.html', form=form)
            login_user(user, remember=True)
            flash("Success!You're logged in.")
            return redirect(url_for("snaps.listing"))
    return render_template('users/login.html', form=form)


@users.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return "Logout successfull"