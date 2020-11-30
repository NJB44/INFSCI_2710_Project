from operator import and_
from os.path import join
from flask.globals import request
from flask.helpers import url_for
from flask_login.utils import login_required
from app.models import doctor, medicine, patient, pharm, pharm_inven, pharm_plant, plant_inven, prescription_order, user, appointment, shipments
from app import db
from flask import render_template, flash, redirect
from app import app
from app.forms import DocPresc, LoginForm, PatNewApt, PharmacyBuy, PharmacySearch, PharmacyShoppingCart, PlantAddStock, PlantEditStock, PlantOrderConf, PlantRemoveStock, RegistrationDocForm, RegistrationPatientForm, RegistrationPharmForm, RegistrationPlantForm
from . import login
from flask_login import current_user, login_user, logout_user
from sqlalchemy import func, desc, asc


@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        usr = db.session.query(user).filter(user.user_id == current_user.user_id).first()
        text = "you are logged in as a " + str(usr.user_type)
    else:
        text = "you are not logged in"
    return render_template('index.html', title='test', text = text)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        usr = db.session.query(user).filter(user.username == form.username.data).first()
        if usr is None or not usr.check_password(password = form.password.data):
            flash('Invalid attempt, please check username or password')
            return redirect('/login')
        login_user(usr)
        #flash('Login requested for user {}'.format{form.username.data})
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/doctor_register', methods=['GET','POST'])
def doctor_register():
    form = RegistrationDocForm()
    if form.validate_on_submit():
        #calculate id here
        highest_id= db.session.query(doctor).order_by(doctor.doc_id.desc()).first()
        highest_id_num = int(highest_id.doc_id[2:])
        id = "DT" + str(highest_id_num + 1)
        doc = doctor(doc_id = id, doc_first_name = form.first_name.data, doc_last_name = form.last_name.data, doc_speciality = form.specialty.data, doc_address = form.address.data, doc_city = form.city.data, doc_state = form.state.data, doc_zipcode = form.zipcode.data)
        usr = user(user_id = id, username = form.username.data , user_type = "doctor")
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
        highest_id= db.session.query(pharm).order_by(pharm.pc_id.desc()).first()
        highest_id_num = int(highest_id.pc_id[2:])
        id = "PC" + str(highest_id_num + 1)
        phrm = pharm(pc_id = id, pc_name = form.name.data, pc_address = form.address.data, pc_city = form.city.data, pc_state = form.state.data, pc_zipcode = form.zipcode.data)
        usr = user(user_id = id, username = form.username.data , user_type = "pharmacy")
        usr.set_password(form.password.data)
        db.session.add(phrm)
        db.session.add(usr)
        db.session.commit()
        flash("You've successfully registered as a pharmacy")
    return render_template('pharmacy_register.html', title = 'Sign In', form = form)

@app.route('/plant_register', methods=['GET','POST'])
def plant_register():
    form = RegistrationPlantForm()
    if form.validate_on_submit():
        #calculate id here
        highest_id= db.session.query(pharm_plant).order_by(pharm_plant.pp_id.desc()).first()
        highest_id_num = int(highest_id.pp_id[2:])
        id = "PP" + str(highest_id_num + 1)
        plant = pharm_plant(pp_id = id, pp_name = form.name.data, pp_address = form.address.data, pp_city = form.city.data, pp_state = form.state.data, pp_zipcode = form.zipcode.data)
        usr = user(user_id = id, username = form.username.data , user_type = "plant")
        usr.set_password(form.password.data)
        db.session.add(plant)
        db.session.add(usr)
        db.session.commit()
        flash("You've successfully registered as a pharmacy plant")
    return render_template('plant_register.html', title = 'Sign In', form = form)

@app.route('/patient_register', methods=['GET','POST'])
def patient_register():
    form = RegistrationPatientForm()
    if form.validate_on_submit():
        #calculate id here
        highest_id= db.session.query(patient).order_by(patient.pat_id.desc()).first()
        highest_id_num = int(highest_id.pat_id[1:])
        id = "P" + str(highest_id_num + 1)
        pat = patient(pat_id = id, doc_id = form.doc_id.data, pat_first_name = form.first_name.data, pat_last_name = form.last_name.data, pat_gender = form.gender.data, pat_ethnicity = form.ethnicity.data, dob = form.dob.data)
        usr = user(user_id = id, username = form.username.data , user_type = "patient")
        usr.set_password(form.password.data)
        db.session.add(pat)
        db.session.add(usr)
        db.session.commit()
        flash("You've successfully registered as a patient")
    return render_template('patient_register.html', title = 'Sign In', form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('index')


######Doctor Pages
@app.route('/doctor_home')
def doc_home():
    return render_template('doctor_home.html')

@app.route('/doctor_home/write_prescription')
def doc_presc():
    #FORM
    form = DocPresc()
    if form.validate_on_submit():
        presc_id = 1 #temp
        order_date = form.order_date.data
        pat_id = form.pat_id.data   
        doc_id = current_user.user_id 
        m_id = form.m_id.data   
        pc_id = form.pc_id.data   
        order_quant = form.order_quant.data
        order_price = 1 #change to query from pharmacy TODO 
        presc = prescription_order(order_id = presc_id, order_status = "pending", order_date = order_date, pat_id = pat_id, doc_id =doc_id, m_id = m_id, pc_id = pc_id, order_quant = order_quant, order_price = order_price)
        db.session.add(prescription_order)
        db.session.commit()

    return render_template('doctor_write_prescription.html', form = form)

@app.route('/doctor_home/check_appointments')
def doc_apt():
    user_id = current_user.user_id 
    doctors_apt = db.session.query(doctor, appointment).filter(user_id == doctor.doc_id).join(appointment, doctor.doc_id == appointment.doc_id).all()
    return render_template('doctor_check_appointments.html', appointments = doctors_apt)

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
        user_id = current_user.user_id
        appointment(apt_id = appointment_id, pat_id = current_user.user_id, doc_id = form.doc_id.data, schedule_day = form.schedule_day.data, apt_date = form.apt_date.data, apt_time = form.apt_time.data)
        db.session.add(appointment)
        db.session.commit()
    return render_template('patient_create_appointment.html', form = form)

@app.route('/patient_home/check_appointments')
def pat_check_apt():
    user_id = current_user.user_id 
    pat_apt = db.session.query(patient, appointment).join(appointment, patient.pat_id == appointment.pat_id).filter(patient.pat_id == user_id).all()
    return render_template('patient_check_appointments.html', appointments = pat_apt)

######Pharmacy Pages
@login_required
@app.route('/pharmacy_home')
def pharm_home():
    return render_template('pharmacy_home.html')

@app.route('/pharmacy_home/pharmacy_inventory')
def pharm_inv():
    pc_id = current_user.user_id 
    inventory = db.session.query(pharm_inven, medicine).filter(pc_id == pharm_inven.pc_id ).join(medicine, pharm_inven.m_id == medicine.m_id).all()
    return render_template('pharmacy_inventory.html', inv = inventory)

@app.route('/pharmacy_home/pharmacy_search',methods=["GET","POST"])
def pharm_search():
    #FORM
    search_form = PharmacySearch()
    checkout_form = PharmacyShoppingCart()
    if search_form.validate_on_submit():
        #send to the browsing page
        ##QUERY here based on form input
        plant_id = search_form.plant.data
        search = "%{}%".format(search_form.search.data) 
        sortby = search_form.sortby.data
        order = search_form.order.data
        if order == "ascending":
            if sortby == "unit_price":
                products = db.session.query(plant_inven, medicine).join(medicine, plant_inven.m_id==medicine.m_id).filter(and_(plant_inven.pp_id == plant_id, medicine.m_medicine.like(search))).order_by(plant_inven.unit_price.asc()).all()
            elif sortby == "stock_quant":
                products = db.session.query(plant_inven, medicine).join(medicine, plant_inven.m_id==medicine.m_id).filter(and_(plant_inven.pp_id == plant_id, medicine.m_medicine.like(search))).order_by(plant_inven.stock_quant.asc()).all()
        elif order == "descending":
            if sortby == "unit_price":
                products = db.session.query(plant_inven, medicine).join(medicine, plant_inven.m_id==medicine.m_id).filter(and_(plant_inven.pp_id == plant_id, medicine.m_medicine.like(search))).order_by(plant_inven.unit_price.desc()).all()
            elif sortby == "stock_quant":
                products = db.session.query(plant_inven, medicine).join(medicine, plant_inven.m_id==medicine.m_id).filter(and_(plant_inven.pp_id == plant_id, medicine.m_medicine.like(search))).order_by(plant_inven.stock_quant.desc()).all()
        else: 
            products = db.session.query(plant_inven, medicine).join(medicine, plant_inven.m_id==medicine.m_id).filter(and_(plant_inven.pp_id == plant_id, medicine.m_medicine.like(search))).all()
        search_form = PharmacySearch()
        return render_template('pharmacy_search.html', search_form= search_form, products = products,checkout_form = checkout_form, checkout = True, search = False)
        #return redirect(url_for('pharm_shop', products=products))
    if checkout_form.validate_on_submit():
        print("Checked out")
        return redirect(url_for('pharmacy_search_history'))
    return render_template('pharmacy_search.html', search_form = search_form, checkout= False, search = True)

#@app.route('/pharmacy_shopping<products>')
#def pharm_shop(plant_id, search, by, order):
#    #QUERY Replace with content from
#    form = PharmacyShoppingCart()
#    #plant_id = current_user.user_id 
#    products = db.session.query(plant_inven, medicine).join(medicine, plant_inven.m_id==medicine.m_id).filter(and_(plant_inven.pp_id == plant_id, medicine.m_medicine.like(search))).all()
#    return render_template('pharmacy_shopping.html', products = products)


#@app.route('/pharmacy_home/pharmacy_med_purchase')
#def pharm_buy(shopping_cart):
#    #FORM
#    form = PharmacyBuy()
#    if form.validate_on_submit():
#        #send to the browsing page
#        pass 
#    return render_template('pharmacy_search.html', form = form, items = shopping_cart)

@app.route('/pharmacy_home/pharmacy_summary')
def pharm_summ():
    #QUERY
    pc_id = current_user.user_id
    unique_med_quant = db.session.query(pharm_inven).filter(pharm_inven.pc_id == pc_id).count()
    total_med_quant = int(db.session.query(func.sum(pharm_inven.quant)).scalar())
    total_inven_value =db.session.query(func.sum(pharm_inven.quant * pharm_inven.price)).scalar()    #TODO query for real summary measures here
    summary_measures = {'unique_medicine_quant': unique_med_quant, 'total_medicine_quant': total_med_quant, 'total_stock_value': total_inven_value}
    return render_template('pharmacy_summary.html', summary_measures = summary_measures)

@app.route('/pharmacy_home/shipment_history')
def pharm_ship_hist():
    #QUERY
    pc_id = current_user.user_id 
    hist_shipments = db.session.query(shipments).filter(pc_id == shipments.pc_id).all()
    return render_template('pharmacy_shipment_history.html', shipments = hist_shipments)

######Plant Pages
@app.route('/plant_home')
def plant_home():
    return render_template('plant_home.html')

@app.route('/plant_home/inventory')
def plant_inv():
    #QUERY
    pp_id = current_user.user_id 
    inventory = db.session.query(plant_inven, medicine).join(medicine, plant_inven.m_id == medicine.m_id).filter(pp_id == plant_inven.pp_id ).all()
    return render_template('plant_inventory.html', inv = inventory)

@app.route('/plant_home/plant_conf')
def plant_order_conf():
    #FORM
    form = PlantOrderConf()
    if form.validate_on_submit():
        pass
    return render_template('plant_conf.html', form = form)

@app.route('/plant_home/plant_shipment_history')
def plant_ship_hist():
    #QUERY
    pp_id = current_user.user_id 
    hist_shipments = db.session.query(shipments).filter(pp_id == shipments.pp_id).all()
    return render_template('plant_shipment_history.html', shipments = hist_shipments)

@app.route('/plant_add_stock', methods = ["GET", "POST"])
def plant_add_stock():
    #FORM
    form = PlantAddStock()
    if form.validate_on_submit():
        new_inven = plant_inven(m_id = form.medicine.data, pp_id = current_user.user_id, stock_quant =  int(form.quantity.data ), unit_price = float(form.unit_price.data))
        db.session.add(new_inven)
        db.session.commit()
        return redirect(url_for('plant_inv'))

    return render_template('plant_add_stock.html', form = form)

@app.route('/plant_edit_stock', methods=["GET", "POST"])
def plant_edit_stock():
    #FORM
    form = PlantEditStock()
    if form.validate_on_submit():
        edited_inven = db.session.query(plant_inven).filter(and_(plant_inven.m_id == form.medicine.data, plant_inven.pp_id == current_user.user_id)).first()
        edited_inven.stock_quant = form.quantity.data
        edited_inven.unit_price = form.unit_price.data
        db.session.commit()
        return redirect(url_for('plant_inv'))

    return render_template('plant_edit_stock.html', form = form)

@app.route('/plant_remove_stock', methods = ["GET", "POST"])
def plant_remove_stock():
    #FORM
    form = PlantRemoveStock()
    if form.validate_on_submit():
        rem_inven = db.session.query(plant_inven).filter(and_(plant_inven.m_id == form.medicine.data, plant_inven.pp_id == current_user.user_id)).first() 
        db.session.delete(rem_inven)
        db.session.commit()
        return redirect(url_for('plant_inv'))

    return render_template('plant_remove_stock.html', form = form)


###misc 
@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')
