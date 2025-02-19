from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError, NumberRange
from pack.models import Registerdb

class Register(FlaskForm):
    def validate_email(self,em):
        obj = Registerdb.query.filter_by(email=em.data).first()
        if obj:
            raise ValidationError('Email Already Registered')

    name = StringField(label='Your name', validators=[Length(min=3,max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Re-enter password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create your account')

class Login(FlaskForm):
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8)])
    submit = SubmitField(label='Sign in')