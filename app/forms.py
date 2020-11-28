from app.models import medicine
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.fields.core import DateField, FloatField, SelectField, TimeField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class RegistrationPharmForm(FlaskForm):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    name = StringField('Pharmacy Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Name must have only letters, ''numbers, dots or underscores')])
    address = StringField('Pharmacy Address', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Address must have only letters, ''numbers, dots or underscores')])
    city = StringField('Pharmacy City', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'City must have only letters')])
    state = StringField('Pharmacy State', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z_.]*$', 0,'State must have only letters')])
    zipcode = IntegerField('Pharmacy Zipcode', validators=[Required()])
    submit = SubmitField("Submit Registration")

class RegistrationPlantForm(FlaskForm):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    name = StringField('Plant Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Name must have only letters, ''numbers, dots or underscores')])
    address = StringField('Plant Address', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Address must have only letters, ''numbers, dots or underscores')])
    city = StringField('Plant City', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'City must have only letters')])
    state = StringField('Plant State', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z_.]*$', 0,'State must have only letters')])
    zipcode = IntegerField('Plant Zipcode', validators=[Required()])
    submit = SubmitField("Submit Registration")

class RegistrationPatientForm(FlaskForm):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    first_name = StringField('Patient First Name', validators=[Required()])
    last_name = StringField('Patient Last Name', validators=[Required()])
    submit = SubmitField("Submit Registration")

class RegistrationDocForm(FlaskForm):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    first_name = StringField('Doctor First Name', validators=[Required()])
    last_name = StringField('Doctor Last Name', validators=[Required()])
    specialty = StringField('Doctor Specialty', validators=[Required()])
    address = StringField('Doctor Address')
    city = StringField('Doctor City')
    state = StringField('Doctor State')
    zipcode = StringField('Doctor Zipcode')
    submit = SubmitField("Submit Registration")

class RegistrationAdminForm(FlaskForm):
    username = StringField('User Name', validators=[Required(), Length(1,20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message = "Passwords must be identical")])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField("Submit Registration")


#####Admin forms
class AdminEditDoctor(FlaskForm):
    doctor_id = StringField('id for account to edit', validators=[Required()])
    first_name = StringField('Doctor First Name', validators=[Required()])
    last_name = StringField('Doctor Last Name', validators=[Required()])
    specialty = StringField('Doctor Specialty', validators=[Required()])
    submit = SubmitField("Complete Edit")

class AdminRemoveDoctor(FlaskForm):
    doctor_id = StringField('id for account to remove', validators=[Required()])
    submit = SubmitField("Remove")

class AdminEditPatient(FlaskForm):
    patient_id = StringField('id for account to edit', validators=[Required()])
    first_name = StringField("Patient First Name")
    last_name = StringField("Patient Last Name")
    address = StringField("Patient Address")
    city = StringField("Patient City")
    state = StringField("Patient State")
    zipcode = StringField("Patient Zipcode")
    submit = SubmitField("Complete Edit")

class AdminRemovePatient(FlaskForm):
    patient_id = StringField('id for account to remove', validators=[Required()])
    submit = SubmitField("Remove")

class AdminEditPharmacy(FlaskForm):
    pharmacy_id = StringField('id for account to edit', validators=[Required()])
    name = StringField('Pharmacy Name')
    address = StringField("Pharmacy Address")
    city = StringField("Pharmacy City")
    state = StringField("Pharmacy State")
    zipcode = StringField("Pharmacy Zipcode")
    submit = SubmitField("Complete Edit")

class AdminRemovePharmacy(FlaskForm):
    pharmacy_id = StringField('id for account to remove', validators=[Required()])
    submit = SubmitField("Submit Registration")

class AdminEditPlant(FlaskForm):
    plant_id = StringField('id for account to edit', validators=[Required()])
    name = StringField('Plant Name')
    address = StringField("Plant Address")
    city = StringField("Plant City")
    state = StringField("Plant State")
    zipcode = StringField("Plant Zipcode")
    submit = SubmitField("Submit Registration")

class AdminRemovePlant(FlaskForm):
    plant_id = StringField('id for account to remove', validators=[Required()])
    submit = SubmitField("Submit Registration")

#####Patient forms
class PatNewApt(FlaskForm):
    doc_id = StringField("enter doctor id here")
    apt_date = DateField('select a day for the appointment', validators=[Required()])
    apt_time = TimeField('select a time for the appointment', validators=[Required()])
    submit = SubmitField("Submit Registration")

#####Doctor forms
class DocPresc(FlaskForm):
    pat_name = StringField('name of patient', validators=[Required()])
    medicine_name = StringField('name of medicine', validators=[Required()])
    pharmacy = SelectField("name of pharmacy", choices=["pharmacy 1", "pharmacy 2"])
    submit = SubmitField("Submit Registration")

#####Pharmacy forms
class PharmacyOrder(FlaskForm):
    quantity = IntegerField('how many of this medicine do you want')
    submit = SubmitField("Submit Registration")

class PharmacySearch(FlaskForm):
    searchbar = StringField("search by medicine name here")
    #query to populate the pharmacy dropdown
    pharmacy = SelectField("select a pharmacy to shop from", choices=["pharmacy 1", "pharmacy 2"])
    sortby = SelectField("sort by", choices=["price", "alphabetical"])
    order = SelectField("order", choices = ["ascending","descending"])
    submit = SubmitField("Submit Registration")

class PharmacyBuy(FlaskForm):
    submit = SubmitField("Submit Registration")

#####Plant forms
class PlantOrderConf(FlaskForm):
    order_status = SelectField("update order status", validators = [Required()], choices = ['In Progress', 'Ready for Shipment', 'Shipped', 'Delivered'])
    submit = SubmitField("Confirm")

class PlantAddStock(FlaskForm):
    medicine = StringField("id of medicine to add", validators=[Required()]) #ought to be a dropdown or validated
    quantity = IntegerField("How many?", validators= [Required()])
    unit_price = FloatField("What price should it be?", validators=[Required()])
    submit = SubmitField("Confirm")

class PlantEditStock(FlaskForm):
    medicine = StringField("id of medicine to edit", validators=[Required()]) #ought to be a dropdown or validated
    unit_price = FloatField("What price should it be?", validators=[Required()])
    submit = SubmitField("Confirm")

class PlantRemoveStock(FlaskForm):
    medicine = StringField("id of medicine to remove", validators=[Required()]) #ought to be a dropdown or validated
    quantity = IntegerField("how many?", validators=[Required()])
    submit = SubmitField("Confirm")

###Misc 
class LoginForm(FlaskForm):
    username = StringField("username", validators=[Required()])
    password = StringField("Password", validators=[Required()])
    submit = SubmitField("Sign in")
