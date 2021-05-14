import flask
import datetime
from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Document):
    user_id    = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name  = db.StringField(max_length=50)
    email      = db.StringField(max_length=50,unique=True)
    uPassword  = db.StringField()
    dob_d      = db.StringField()
    dob_m      = db.StringField()
    dob_y      = db.StringField()
    gender     = db.StringField()
    MedQual    = db.StringField()
    MedLicN    = db.StringField()
    c_add      = db.StringField(max_length=100)
    c_city     = db.StringField(max_length=30)
    c_country  = db.StringField(max_length=30)
    c_pincode  = db.StringField(max_length=6)
    
    def set_password(self,password):
        self.uPassword=generate_password_hash(password)
    
    def get_password(self,password):
        return check_password_hash(self.uPassword,password)
    
class Patient_data(db.Document):
    patient_id = db.StringField()
    doctor_id  = db.StringField()
    first_name = db.StringField(max_length=50)
    last_name  = db.StringField(max_length=50)
    email      = db.StringField(max_length=50,unique=True)
    pPassword  = db.StringField()
    dob_d      = db.StringField()
    dob_m      = db.StringField()
    dob_y      = db.StringField()
    gender     = db.StringField()
    govID_type = db.StringField()
    govID      = db.StringField()
    p_add      = db.StringField(max_length=30)
    p_city     = db.StringField(max_length=30)
    p_country  = db.StringField(max_length=30)
    p_pincode  = db.StringField(max_length=6)
    p_diagnosys= db.StringField(max_length=500)
    
    def pset_password(self,password):
        self.pPassword=generate_password_hash(password)
    
    def pget_password(self,password):
        return check_password_hash(self.pPassword,password)
    
class Doctor_patient_allotment(db.Document):
    doctor_id  = db.IntField()
    patient_id  = db.StringField()
    
class Patient_Device_Data(db.Document):
    finger1      = db.IntField()
    finger2      = db.IntField()
    finger3      = db.IntField()
    finger4      = db.IntField()
    finger5      = db.IntField()
    tempMax      = db.IntField()
    tempMin      = db.IntField()
    tempAvg      = db.IntField()
    EventTrigger = db.IntField()
    timestamp    = db.DateTimeField(required=True, default=datetime.datetime.now)
    def my_save(object):
        object.updated_at = datetime.datetime.now()
        return object.save()