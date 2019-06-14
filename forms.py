from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, EqualTo,Email
from wtforms import ValidationError


class LoginForm(FlaskForm):

    username= StringField('User-Name:- ', validators=[DataRequired()])
    password= PasswordField('Password:- ', validators=[DataRequired()])
    submit =SubmitField('Log in')


class RegisterForm(FlaskForm):

    email= StringField('Email', validators=[DataRequired(), Email()] )
    username= StringField('User-Name:- ', validators=[DataRequired()])
    password= PasswordField('Password:- ', validators=[DataRequired(), EqualTo('confirm_pass', message='Password must match!')])
    confirm_pass= PasswordField('Confirm Password:- ', validators=[DataRequired()])
    submit =SubmitField('Register')

    def check_email(self, field):

        if User.query.filter_by(email= field.data).first():
            raise ValidationError('Your email has been registered!')


    def check_username(self, field):

        if User.query.filter_by(username= field.data).first():
            raise ValidationError('Your username has been registered!')
