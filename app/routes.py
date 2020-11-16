from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RegistrationAdminForm, RegistrationDocForm, RegistrationPatientForm, RegistrationPharmForm, RegistrationPlantForm
from . import login_manager
from flask_login import logout_user


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'test'}
    return render_template('index.html', title='test', user = user)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #flash('Login requested for user {}'.format{form.username.data})
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/doctor_register', methods=['GET','POST'])
def doctor_register():
    form = RegistrationDocForm()
    return render_template('doctor_register.html', title = 'Sign In', form = form)

@app.route('/pharmacy_register', methods=['GET','POST'])
def pharmacy_register():
    form = RegistrationPharmForm()
    return render_template('pharmacy_register.html', title = 'Sign In', form = form)

@app.route('/plant_register', methods=['GET','POST'])
def plant_register():
    form = RegistrationPlantForm()
    return render_template('plant_register.html', title = 'Sign In', form = form)

@app.route('/patient_register', methods=['GET','POST'])
def patient_register():
    form = RegistrationPatientForm()
    return render_template('patient_register.html', title = 'Sign In', form = form)

@app.route('/admin_register', methods=['GET','POST'])
def admin_register():
    form = RegistrationAdminForm()
    return render_template('admin_register.html', title = 'Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('index.html')

######Admin Pages
@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@app.route('/admin_home/edit_doctor')
def edit_doc():
    #FORM
    return render_template('edit_doctor.html')

@app.route('/admin_home/remove_doctor')
def rem_doc():
    #FORM
    return render_template('remove_doctor.html')

@app.route('/admin_home/edit_patient')
def edit_pat():
    #FORM
    return render_template('edit_patient.html')

@app.route('/admin_home/remove_patient')
def rem_pat():
    #FORM
    return render_template('remove_patient.html')

@app.route('/admin_home/edit_pharmacy')
def edit_pharm():
    #FORM
    return render_template('edit_pharmacy.html')

@app.route('/admin_home/remove_pharmacy')
def rem_pharm():
    #FORM
    return render_template('remove_pharmacy.html')

@app.route('/admin_home/edit_plant')
def edit_plant():
    #FORM
    return render_template('edit_plant.html')

@app.route('/admin_home/remove_plant')
def rem_plant():
    #FORM
    return render_template('remove_plant.html')


######Doctor Pages
@app.route('/doctor_home')
def doc_home():
    return render_template('doctor_home.html')

@app.route('/doctor_home/write_prescription')
def doc_presc():
    #FORM
    return render_template('doctor_write_prescription.html')

@app.route('/doctor_home/check_appointments')
def doc_apt():
    #QUERY
    return render_template('doctor_check_appointments.html')


######Patient Pages
@app.route('/patient_home')
def pat_home():
    return render_template('patient_home.html')

@app.route('/patient_home/create_appointment')
def pat_new_apt():
    #FORM
    return render_template('patient_create_appointment.html')

@app.route('/patient_home/check_appointments')
def pat_check_apt():
    #QUERY
    return render_template('patient_check_appointments.html')


######Pharmacy Pages
@app.route('/pharmacy_home')
def pharm_home():
    return render_template('pharmacy_home.html')

@app.route('/pharmacy_home/pharmacy_inventory')
def pharm_inv():
    #QUERY
    return render_template('pharmacy_inventory.html')

@app.route('/pharmacy_home/shipment_history')
def pharm_ship_hist():
    #QUERY
    return render_template('shipment_history.html')

@app.route('/pharmacy_home/shopping')
def pharm_shop():
    #QUERY
    return render_template('pharmacy_shopping.html')


######Plant Pages
@app.route('/plant_home')
def plant_home():
    #FORM
    return render_template('plant_home.html')

@app.route('/plant_home/inventory')
def plant_inv():
    #QUERY
    return render_template('plant_inventory.html')

@app.route('/plant_home/order_confirmation')
def plant_order_conf():
    #FORM
    return render_template('plant_order_confirmation.html')

@app.route('/plant_home/shipment_history')
def plant_ship_hist():
    #QUERY
    return render_template('plant_shipment_history.html')

@app.route('/plant_add_stock')
def plant_add_stock():
    #FORM
    return render_template('plant_add_stock.html')