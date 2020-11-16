from datetime import datetime
from app import db 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class user(UserMixin ,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), index=True, unique = True)
    user_type = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class pharm_plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zipcode = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Plant {}>'.format(self.name)

class medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    name = db.Column(db.String(64))
    ingredient = db.Column(db.String(64))

    def __repr__(self):
        return '<Medicine {}>'.format(self.name)


class plant_inven(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    m_id = db.Column(db.Integer, db.ForeignKey("medicine.id")) #prim key
    pp_id = db.Column(db.Integer, db.ForeignKey("pharmacy.id")) #prim key
    stock_quant = db.Column(db.Integer)
    unit_price = db.Column(db.Integer)

    def __repr__(self):
        return '<plant inventory {}>'.format(self.pp_id)


class shipments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pp_id = db.Column(db.Integer,db.ForeignKey("plant.id"))
    m_id = db.Column(db.Integer,db.ForeignKey("medicine.id"))
    pc_id = db.Column(db.Integer,db.ForeignKey("pharmacy.id"))
    quant = db.Column(db.Integer)
    price = db.Column(db.Float) #CHECK THIS
    order_date = db.Column(db.Date) #CHECK THIS
    ship_date = db.Column(db.Date) #CHECK THIS
    delivery_date = db.Column(db.Date) #CHECK THIS

    def __repr__(self):
        return '<Shipment {}>'.format(self.order_num)


class pharm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zipcode = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Pharmacy {}>'.format(self.name)


class pharm_inven(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pc_id = db.Column(db.Integer, db.ForeignKey("pharmacy.id")) #prim key
    m_id = db.Column(db.Integer, db.ForeignKey("medicine.id") ) #prim key
    quant = db.Column(db.Integer)
    price = db.Column(db.Float) #CHECK THIS

    def __repr__(self):
        return '<Pharmacy Inventory {}>'.format(pc_id.username)


class prescription_order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date) #CHECK THIS
    pat_id = db.Column(db.Integer,db.ForeignKey("patient.id"))
    doc_id = db.Column(db.Integer,db.ForeignKey("doctor.id"))
    m_id = db.Column(db.Integer,db.ForeignKey("medicine.id"))
    quant = db.Column(db.Integer)
    price = db.Column(db.Float) #CHECK THIS

    def __repr__(self):
        return '<prescription order {}>'.format(self.order_id)


class patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.Integer,db.ForeignKey("doctor.id"))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    gender = db.Column(db.String(1)) #CHECK THIS
    ethnicity = db.Column(db.String(64))
    dob = db.Column(db.Date) #CHECK THIS
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zipcode = db.Column(db.Integer)
    pat_first_visit_date = db.Column(db.Date) #CHECK THIS
    doc_off_id = db.Column(db.Integer,db.ForeignKey("doctor_office.id"))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Patient {}>'.format(self.last_name)


class prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pat_first_name = db.Column(db.String(64))
    pat_last_name = db.Column(db.String(64))
    pat_id= db.Column(db.Integer,db.ForeignKey("patient.id"))
    apt_date = db.Column(db.Date) #CHECK THIS
    m_id = db.Column(db.Integer,db.ForeignKey("medicine.id"))
    m_name = db.Column(db.String(64))
    doc_name = db.Column(db.String(64))
    doc_id = db.Column(db.Integer,db.ForeignKey("doctor.id"))
    doc_off_id = db.Column(db.Integer, db.ForeignKey('doctor_office.id'))

    def __repr__(self):
        return '<prescription name {} for patient {}>'.format(self.m_name, self.pat_last_name)


class appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pat_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    doc_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    doc_off_id = db.Column(db.Integer, db.ForeignKey('doctor_office.id'))
    date = db.Column(db.Date) #CHECK THIS
    time = db.Column(db.Time) #CHECK THIS

    def __repr__(self):
        return '<Doctor number {} on {} at {} >'.format(self.doc_id, self.date, self.time)


class doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    specialty = db.Column(db.String(64))
    doc_off_id = db.Column(db.Integer, db.ForeignKey('doctor_office.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Dr. {}>'.format(self.last_name)


class doctor_office(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facility_name = db.Column(db.String(64))
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zipcode = db.Column(db.Integer)

    def __repr__(self):
        return '<Office {}>'.format(self.facility_name)
