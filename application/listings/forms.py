from wtforms import (Form, 
                     StringField, 
                     PasswordField,
                     HiddenField, 
                     validators, 
                     SubmitField)
from wtforms.validators import (ValidationError, 
                                DataRequired, 
                                Email, 
                                EqualTo, 
                                Length, 
                                Optional)
from wtforms_components import EmailField


class ListingForm(Form):
    name = StringField('name', validators=[DataRequired(message=('Enter Listing name'))])
    address = StringField('address', validators=[DataRequired(message=('Enter Listing Address'))])
