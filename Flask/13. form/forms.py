from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name = TextField("Name of Student", [validators.Required("Please enter yout name.")])
    Gender = RadioField('Gender', choices = [('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField('Address')
    email = TextField('Email', [validators.Required('Please enter your email address'), validators.Email('Please enter your correct email')])
    Age = IntegerField('Age')
    language = SelectField('Language', choices = [('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField('Send')