from flask.globals import request
from flask.helpers import url_for
from app.models import doctor, medicine, patient, pharm, pharm_inven, pharm_plant, plant_inven, user, appointment
from app import db
from flask import render_template, flash, redirect
from app import app
from app.forms import AdminEditDoctor, AdminEditPatient, AdminEditPharmacy, AdminEditPlant, AdminRemoveDoctor, AdminRemovePatient, AdminRemovePharmacy, AdminRemovePlant, DocPresc, LoginForm, PatNewApt, PharmacySearch, PlantAddStock, PlantEditStock, PlantOrderConf, PlantRemoveStock, RegistrationAdminForm, RegistrationDocForm, RegistrationPatientForm, RegistrationPharmForm, RegistrationPlantForm
from . import login
from flask_login import current_user, login_user, logout_user


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'test'}
    return render_template('index.html', title='test', user = user)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        usr = user.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid attempt, please check username or password')
        login_user(user)
        #flash('Login requested for user {}'.format{form.username.data})
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/doctor_register', methods=['GET','POST'])
def doctor_register():
    form = RegistrationDocForm()
    if form.validate_on_submit():
        #calculate id here
        id = 1 #temporary
        doc = doctor(doc_id = id, doc_first_name = form.first_name.data, doc_last_name = form.last_name.data, doc_specificity = form.specialty.data, doc_address = form.address.data, doc_city = form.city.data, doc_state = form.state.data, doc_zipcode = form.zipcode.data)
        usr = user(u_id = id, username = form.username.data , user_type = "doctor")
        usr.set_password(form.password.data)
        db.session.add(doc)
        db.session.add(usr)
        db.session.commit()
        flash("You've successfully registered as a doctor")
    return render_template('doctor_register.html', title = 'Sign In', form = form)

@app.route('/pharmacy_register', methods=['GET','POST'])
def pharmacy_register():
    form = RegistrationPharmForm()
    if form.validate_on_submit():
        #calculate id here
        id = 1 #temporary
        phrm = pharm(pc_id = id, pc_name = form.name.data, pc_address = form.address.data, pc_city = form.city.data, pc_state = form.state.data, pc_zipcode = form.zipcode.data)
        usr = user(u_id = id, username = form.username.data , user_type = "pharmacy")
        usr.set_password(form.password.data)
        db.session.add(phrm)
        db.session.add(usr)
        flash("You've successfully registered as a pharmacy")
    return render_template('pharmacy_register.html', title = 'Sign In', form = form)

@app.route('/plant_register', methods=['GET','POST'])
def plant_register():
    form = RegistrationPlantForm()
    if form.validate_on_submit():
        #calculate id here
        id = 1 #temporary
        plant = pharm_plant(pp_id = id, pp_name = form.name.data, pp_address = form.address.data, pp_city = form.city.data, pp_state = form.state.data, pp_zipcode = form.zipcode.data)
        usr = user(u_id = id, username = form.username.data , user_type = "plant")
        usr.set_password(form.password.data)
        db.session.add(plant)
        db.session.add(usr)
        flash("You've successfully registered as a pharmacy plant")
    return render_template('plant_register.html', title = 'Sign In', form = form)

@app.route('/patient_register', methods=['GET','POST'])
def patient_register():
    form = RegistrationPatientForm()
    if form.validate_on_submit():
        #calculate id here
        id = 1 #temporary
        pat = patient(pat_id = id, pat_first_name = form.first_name.data, pat_last_name = form.last_name.data)
        usr = user(u_id = id, username = form.username.data , user_type = "patient")
        usr.set_password(form.password.data)
        db.session.add(pat)
        db.session.add(usr)
        flash("You've successfully registered as a patient")
    return render_template('patient_register.html', title = 'Sign In', form = form)

@app.route('/admin_register', methods=['GET','POST'])
def admin_register():
    form = RegistrationAdminForm()
    if form.validate_on_submit():
        #calculate id here
        id = 1 #temporary
        usr = user(u_id = id, username = form.username.data , user_type = "admin")
        usr.set_password(form.password.data)
        db.session.add(usr)
        flash("You've successfully registered as an admin")
    return render_template('admin_register.html', title = 'Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('index.html')

######Admin Pages
@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@app.route('/admin_home/edit_doctor', methods = ['GET','POST'])
def edit_doc():
    form = AdminEditDoctor()
    #FORM
    if form.validate_on_submit():
        edited_doc = db.session.query(doctor).filter_by(doctor_id = form.doctor_id.data).first()
        edited_doc.first_name = form.first_name.data
        edited_doc.last_name = form.last_name.data
        edited_doc.specialty = form.specialty.data
        db.session.commit()
        flash('doctor information has been updated')
    elif request.method =='GET':
        #edited_doc = db.session.query(doctor).filter_by(doctor_id = form.doctor_id.data).first()
        form.first_name.data
       
    return render_template('edit_doctor.html', form=form)

@app.route('/admin_home/remove_doctor')
def rem_doc():
    form = AdminRemoveDoctor()
    if form.validate_on_submit():
        pass
    #FORM
    return render_template('remove_doctor.html', form = form)

@app.route('/admin_home/edit_patient', methods = ['GET','POST'])
def edit_pat():
    #FORM
    form = AdminEditPatient()
    if form.validate_on_submit():
        pass
    return render_template('edit_patient.html', form = form)

@app.route('/admin_home/remove_patient')
def rem_pat():
    #FORM
    form = AdminRemovePatient()
    if form.validate_on_submit():
        pass
    return render_template('remove_patient.html', form = form)

@app.route('/admin_home/edit_pharmacy', methods = ['GET', 'POST'])
def edit_pharm():
    #FORM
    form = AdminEditPharmacy()
    if form.validate_on_submit():
        pass
    return render_template('edit_pharmacy.html', form = form)

@app.route('/admin_home/remove_pharmacy')
def rem_pharm():
    #FORM
    form = AdminRemovePharmacy()
    if form.validate_on_submit():
        pass
    return render_template('remove_pharmacy.html', form = form)

@app.route('/admin_home/edit_plant', methods = ['GET','POST'])
def edit_plant():
    #FORM
    form = AdminEditPlant()
    if form.validate_on_submit():
        pass
    return render_template('edit_plant.html', form = form)

@app.route('/admin_home/remove_plant')
def rem_plant():
    #FORM
    form = AdminRemovePlant()
    if form.validate_on_submit():
        pass
    return render_template('remove_plant.html', form = form)


######Doctor Pages
@app.route('/doctor_home')
def doc_home():
    return render_template('doctor_home.html')

@app.route('/doctor_home/write_prescription')
def doc_presc():
    #FORM
    form = DocPresc()
    if form.validate_on_submit():
        pass
    return render_template('doctor_write_prescription.html', form = form)

@app.route('/doctor_home/check_appointments')
def doc_apt():
    #QUERY
    doctors_apt = db.session.query(doctor, appointment).join(appointment, doctor.doc_id == appointment.doc_id)
    return render_template('doctor_check_appointments.html', apts = doctors_apt)


######Patient Pages
@app.route('/patient_home')
def pat_home():
    return render_template('patient_home.html')

@app.route('/patient_home/create_appointment')
def pat_new_apt():
    #FORM
    form = PatNewApt()
    if form.validate_on_submit():
        appointment_id = 1 #replace with code to properly generate this
        user_id = current_user.id
        appointment(apt_id = appointment_id, pat_id = current_user.id, doc_id = form.doc_id.data, schedule_day = form.schedule_day.data, apt_date = form.apt_date.data, apt_time = form.apt_time.data)
        db.session.add(appointment)
        db.session.commit()
    return render_template('patient_create_appointment.html', form = form)

@app.route('/patient_home/check_appointments')
def pat_check_apt():
    #QUERY
    user_id = current_user.id
    pat_apt = db.session.query(patient, appointment).join(appointment, patient.pat_id == appointment.pat_id).filter(pat_id = user_id).all()
    return render_template('doctor_check_appointments.html', apts = pat_apt)


######Pharmacy Pages
@app.route('/pharmacy_home')
def pharm_home():
    return render_template('pharmacy_home.html')

@app.route('/pharmacy_home/pharmacy_inventory')
def pharm_inv():
    #QUERY
    inventory = db.session.query(pharm_inven, medicine).join(medicine, pharm_inven.m_id == medicine.m_id).filter_by(pc_id = current_user.id)
    return render_template('pharmacy_inventory.html', inv = inventory)

@app.route('/pharmacy_home/pharmacy_search')
def pharm_search():
    #FORM
    form = PharmacySearch()
    if form.validate_on_submit():
        #send to the browsing page
        pass 
    return render_template('pharmacy_search.html', form = form)

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
    return render_template('plant_home.html')

@app.route('/plant_home/inventory')
def plant_inv():
    #QUERY
    return render_template('plant_inventory.html')

@app.route('/plant_home/plant_conf')
def plant_order_conf():
    #FORM
    form = PlantOrderConf()
    if form.validate_on_submit():
        pass
    return render_template('plant_conf.html', form = form)

@app.route('/plant_home/shipment_history')
def plant_ship_hist():
    #QUERY
    return render_template('plant_shipment_history.html')

@app.route('/plant_add_stock')
def plant_add_stock():
    #FORM
    form = PlantAddStock()
    if form.validate_on_submit():
        plant_inven(m_id = form.medicine.data, pp_id = current_user.id, stock_quant =  form.quantity.data, unit_price = form.unit_price.data)
        db.session.add(plant_inven)
        db.session.commit()

    return render_template('plant_add_stock.html', form = form)

@app.route('/plant_edit_stock', methods=["GET", "POST"])
def plant_edit_stock():
    #FORM
    form = PlantEditStock()
    if form.validate_on_submit():
        plant_inven(m_id = form.medicine.data, pp_id = current_user.id, stock_quant =  form.quantity.data, unit_price = form.unit_price.data)
        db.session.add(plant_inven)
        db.session.commit()

    return render_template('plant_edit_stock.html', form = form)

@app.route('/plant_remove_stock')
def plant_remove_stock():
    #FORM
    form = PlantRemoveStock()
    return render_template('plant_remove_stock.html', form = form)
