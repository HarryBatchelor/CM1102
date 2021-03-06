from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^.{6,10}$', message='Your password should be between 6 and 10 characters long')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')

class ReviewForm(FlaskForm):
	user_name = StringField('Username', validators=[DataRequired()])
	body = StringField('Review', validators=[DataRequired()])
	submit = SubmitField('Submit')


def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('This email is already registered.\ please choose a differnt one')

def validate_Username(self, username):
    user = User.Query.filter_by(username=username.data).first()
    if user:
        raise ValidationError('This username is alreadt taken\ Please choose a differnt one')
