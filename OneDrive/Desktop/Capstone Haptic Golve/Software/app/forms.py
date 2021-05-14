from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SubmitField,RadioField,FileField
from wtforms.validators import DataRequired,Email,Length,EqualTo,ValidationError
from app.models import User

class LoginForm(FlaskForm):
    email    = StringField("Email",validators=[DataRequired(),Email()],render_kw={"class": "in" , "placeholder":"Email"})
    password = PasswordField("Password",validators=[DataRequired(),Length(min=6)],render_kw={"class": "in","placeholder":"Password"})
    submit   = SubmitField("Login",render_kw={"class": "x"})

class RegisterForm(FlaskForm):
    first_name = StringField("First Name",validators=[DataRequired()],render_kw={"placeholder":"First Name"})
    last_name  = StringField("Last Name",validators=[DataRequired()],render_kw={"placeholder":"Last Name"})
    email      = StringField("Email",validators=[DataRequired(),Email()],render_kw={"class": "" , "placeholder":"Email"})
    uPassword  = PasswordField("Password",validators=[DataRequired(),Length(min=6,max=30)],render_kw={"class": "","placeholder":"Password"})
    dob_d      = StringField("dob_d",validators=[DataRequired()],render_kw={"placeholder":"DD"})
    dob_m      = StringField("dob_m",validators=[DataRequired()],render_kw={"placeholder":"MM"})
    dob_y      = StringField("dob_y",validators=[DataRequired()],render_kw={"placeholder":"YYYY"})
    gender     = RadioField('Gender', choices=[('Male','Male'),('Female','Female')], render_kw={"style":"list-style-type: none; padding:0px"})
    MedQual    = RadioField('MedQual', choices=[('Doctor','Doctor'),('Physiotherapist','Physiotherapist')], render_kw={"style":"list-style-type: none; padding:0px"})
    MedLicN    = StringField("MedLicN",validators=[DataRequired()],render_kw={"placeholder":"Medical license Number"})
    c_add      = StringField("Address",validators=[DataRequired()],render_kw={"placeholder":"Address"})
    c_city     = StringField("City",validators=[DataRequired()],render_kw={"placeholder":"City"})
    c_country  = StringField("Country",validators=[DataRequired()],render_kw={"placeholder":"Country"})
    c_pincode  = StringField("Pincode",validators=[DataRequired()],render_kw={"placeholder":"Pincode"})
    prodp      = FileField()
    submit     = SubmitField("Register",render_kw={"class": "subl"})
    
    def validate_email(self,email):
        user=User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another Email.")

class PatintRegisterForm(FlaskForm):
    first_name = StringField("First Name",validators=[DataRequired()])
    last_name  = StringField("Last Name",validators=[DataRequired()])
    doctor_id  = StringField("Doctor ID",validators=[DataRequired()])
    email      = StringField("Email",validators=[DataRequired()])
    uPassword  = StringField("Password",validators=[DataRequired()])
    dob_d      = StringField("dob_d",validators=[DataRequired()])
    dob_m      = StringField("dob_m",validators=[DataRequired()])
    dob_y      = StringField("dob_y",validators=[DataRequired()])
    gender     = StringField("gender",validators=[DataRequired()])
    MedQual    = StringField("MedQual",validators=[DataRequired()])
    MedLicN    = StringField("MedLicN",validators=[DataRequired()])
    c_add      = StringField("Address",validators=[DataRequired()])
    c_city     = StringField("City",validators=[DataRequired()])
    c_country  = StringField("Country",validators=[DataRequired()])
    c_pincode  = StringField("Pincode",validators=[DataRequired()])
    submit     = SubmitField("Register")