from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class RegistrationPharmForm(Form):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    name = StringField('Pharmacy Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Name must have only letters, ''numbers, dots or underscores')])
    address = StringField('Pharmacy Address', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Address must have only letters, ''numbers, dots or underscores')])
    city = StringField('Pharmacy City', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'City must have only letters')])
    state = StringField('Pharmacy State', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z_.]*$', 0,'State must have only letters')])
    zipcode = IntegerField('Pharmacy Zipcode', validators=[Required()])
    submit = SubmitField("Submit Registration")

class RegistrationPlantForm(Form):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    name = StringField('Plant Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Name must have only letters, ''numbers, dots or underscores')])
    address = StringField('Plant Address', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Address must have only letters, ''numbers, dots or underscores')])
    city = StringField('Plant City', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'City must have only letters')])
    state = StringField('Plant State', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z_.]*$', 0,'State must have only letters')])
    zipcode = IntegerField('Plant Zipcode', validators=[Required()])
    submit = SubmitField("Submit Registration")


class RegistrationPatientForm(Form):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    first_name = StringField('Patient First Name', validators=[Required()])
    last_name = StringField('Patient Last Name', validators=[Required()])
    submit = SubmitField("Submit Registration")

class RegistrationDocForm(Form):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    first_name = StringField('Doctor First Name', validators=[Required()])
    last_name = StringField('Doctor Last Name', validators=[Required()])
    specialty = StringField('Doctor Specialty', validators=[Required()])
    #office_id = StringField('Doctor Office id') do we need this?
    submit = SubmitField("Submit Registration")

class RegistrationAdminForm(Form):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField("Submit Registration")


class LoginForm(FlaskForm):
    username = StringField("username", validators=[Required()])
    password = StringField("Password", validators=[Required()])
    submit = SubmitField("Sign in")

class PharmacyMedicinePurchase(FlaskForm):
    username = StringField("username", validators=[Required()])