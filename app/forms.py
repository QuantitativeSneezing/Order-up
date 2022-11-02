from flask_wtf import FlaskForm
from wtforms.fields import  StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime


class LoginForm(FlaskForm):
    employee_number = StringField("Employee Number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
