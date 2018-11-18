from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,SelectMultipleField
from wtforms.validators import ValidationError,DataRequired, Length, Email, EqualTo
from flaskblog.models import User

my_choices = [('1', 'Choice1'), ('2', 'Choice2'), ('3', 'Choice3'),
            ('1', 'Choice1'), ('2', 'Choice2'), ('3', 'Choice3'),
            ('1', 'Choice1'), ('2', 'Choice2'), ('3', 'Choice3')]

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    interests=SelectMultipleField('Interests',choices=my_choices,default = ['1'])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken')
    def validate_email(self,email):
        user=User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('Email already taken')




class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')