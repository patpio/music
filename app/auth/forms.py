from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from flask_babel import lazy_gettext as _l

from .models import User


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username *'), validators=[
        InputRequired(_l('Input is required.')),
        DataRequired(_l('Data is required.')),
        Length(3, 20, message=_l('Username must be between 3 and 20 characters long.'))
    ])
    email = EmailField(_l('Email *'), validators=[
        InputRequired(_l('Input is required.')),
        DataRequired(_l('Data is required.')),
        Length(6, 30, message=_l('Username must be between 3 and 20 characters long.')),
        Email(_l('You did not enter a valid email!'))
    ])
    password = PasswordField(_l('Password *'), validators=[
        InputRequired(_l('Input is required.')),
        DataRequired(_l('Data is required.')),
        Length(6, 30, message=_l('Password must be between 3 and 20 characters long.')),
        EqualTo('password_confirm', message=_l('Password must match.'))
    ])
    password_confirm = PasswordField(_l('Repeat your password *'), validators=[DataRequired()])
    submit = SubmitField(_l('Register'))

    @staticmethod
    def validate_username(form, field):  # form -> self -> form object
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(_l('Username already exist.'))

    @staticmethod
    def validate_email(form, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(_l('Email already taken.'))


class LoginForm(FlaskForm):
    email = EmailField(_l('Your email *'), validators=[
        InputRequired(_l('Input is required.')),
        DataRequired(_l('Data is required.')),
        Length(6, 30, message=_l('Username must be between 3 and 20 characters long.')),
        Email(_l('You did not enter a valid email!'))
    ])
    password = PasswordField(_l('Your password: '), validators=[
        InputRequired(_l('Input is required.')),
        DataRequired(_l('Data is required.')),
        Length(6, 30, message=_l('Username must be between 3 and 20 characters long.')),
    ])
    remember_me = BooleanField(_l('Keep me logged in.'))
    submit = SubmitField(_l('Login'))