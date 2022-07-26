from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")


class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    name = StringField("Complete Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember_me = BooleanField("remember_me")
