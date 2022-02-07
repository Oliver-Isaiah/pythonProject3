from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import InputRequired

class loginForm(Form):
    username = StringField('UserName',validators=[InputRequired()])
    password = PasswordField('PassWord',validators=[InputRequired()])
    submit = SubmitField('login')