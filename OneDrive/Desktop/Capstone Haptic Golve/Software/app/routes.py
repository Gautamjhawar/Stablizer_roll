from flask.helpers import flash
from app import app, db, api
from flask import render_template, redirect, request, session, json, Response, flash, jsonify
from app.models import User, Patient_data, Doctor_patient_allotment, Patient_Device_Data
from app.forms import LoginForm,RegisterForm,PatintRegisterForm
from flask_restx import Resource

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login",methods=['GET','POST'])
#@app.route("/Login")
def login():
    if session.get('uName'):
        x=session['uName']
        flash(f"{x} You are already logged in!!","danger")
        return redirect("/dashboard")
    lform=LoginForm()
    if lform.validate_on_submit():
        email    = lform.email.data
        password = lform.password.data
        
        user =User.objects(email=email).first()
        
        if user and user.get_password(password):
            flash("You are successfully logged in!!", "success")
            session['user_id']=user.user_id
            session['uName']=user.first_name
            return redirect("/dashboard")
        else:
            flash(" Please Check your Email and password","danger")
    return render_template("login.html",form=lform)

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('uName',None)
    flash(" Successfully logged out!","success")
    return redirect("/home")

@app.route("/register",methods=['GET','POST'])
def register():
    if session.get('uName'):
        x=session['uName']
        flash(f"{x} You are already logged in!!","danger")
        return redirect("/dashboard")
    rform=RegisterForm()
    if rform.validate_on_submit():
        user_id= User.objects.count()
        user_id+=1
        email =rform.email.data
        first_name = rform.first_name.data
        last_name  = rform.last_name.data
        uPassword  = rform.uPassword.data
        dob_d      = rform.dob_d.data
        dob_m      = rform.dob_m.data
        dob_y      = rform.dob_y.data
        gender     = rform.gender.data
        MedQual    = rform.MedQual.data
        MedLicN    = rform.MedLicN.data
        c_add      = rform.c_add.data
        c_city     = rform.c_city.data
        c_country  = rform.c_country.data
        c_pincode  = rform.c_pincode.data
        user=User(user_id=user_id,email=email,first_name=first_name,last_name=last_name,dob_d=dob_d,dob_m=dob_m,dob_y=dob_y,gender=gender,MedLicN=MedLicN,MedQual=MedQual,c_pincode=c_pincode,c_add=c_add,c_city=c_city,c_country=c_country)
        user.set_password(uPassword)
        user.save()
        flash("You registered successfully!!","success")
        return redirect("/login")
    # else:
    #     flash(" Something went wrong try again","danger")
    return render_template("register.html",form=rform)

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/poster")
def poster():
    return render_template("poster.html")

@app.route("/paper")
def paper():
    return render_template("paper.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/dashboard")
def dashboard():
    if not session.get('uName'):
        flash(" You are not logged in, Sign in first","danger")
        return redirect("/login")
    uid=session.get('user_id')
    userloggedin=session.get('uName')
    return render_template("testanalytics.html",data=userloggedin)

    
@app.route("/user")
def user():
    #User(user_id=1,first_name='Gautam',last_name='Jhawar',email="jhawargautam@gmail.com",uPassword="test1234",dob_d="20",dob_m="10",dob_y="1999",gender="Male",MedQual='Doctor',MedLicN="ASDF14526F",c_add="10,villa",c_city='Secunderabad',c_country="India",c_pincode="500087").save()
    #User(user_id=2,first_name='kanji',last_name='nakamura',email="kanji@rediff.com",uPassword="test4569",dob_d="20",dob_m="1",dob_y="1989",gender="Female",MedQual='Doctor',MedLicN="ASDF14526F",c_add="10,villa",c_city='Secunderabad',c_country="India",c_pincode="500087").save()
    users=User.objects.all()
    return render_template("user.html",users=users)

############ API ##############

@api.route('/api/getuserobject')
class GetandPost(Resource):
    
    # def get(self):
    #     return jsonify(User.objects.all())
    
    def post(self):
        data=api.payload
        print(api.payload)
        dframe=Patient_Device_Data(finger1=data['finger1'],finger2=data['finger2'],finger3=data['finger3'],finger4=data['finger4'],finger5=data['finger5'],tempMax=data['tempMax'],tempMin=data['tempMin'],tempAvg=data['tempAvg'],EventTrigger=data['EventTrigger'])
        dframe.my_save()
        return jsonify("200 OK")
    
# @api.route('/api/getuserobject/<idx>')
# class Getupdatedelete(Resource):
    
#     def get(self,idx):
#         return jsonify(User.objects(user_id=idx))
    
    
