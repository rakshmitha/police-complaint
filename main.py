from flask import Flask,render_template, request, redirect,session
import dbservice as dbs
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def home():
    if 'user_id' not in session:
        return render_template('login.html')
    else:
        history=dbs.get_history()
        return render_template('dashboard.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    history=dbs.get_history()
    return render_template('dashboard.html', history=history)


@app.route('/login_validation', methods=['POST','GET'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    myuser_id=dbs.login(email, password)
    if myuser_id==-1:
        return render_template('login.html')   
    else:
        session['user_id']=myuser_id
        return redirect('/')

@app.route('/add_user', methods=['POST','GET'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    myuser_id=dbs.add_user(name, email, password)
    session['user_id']=myuser_id
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear() 
    return redirect('/')

@app.route('/register_complaint')
def register_complaint():
    return render_template('/register_complaint.html')

@app.route('/incident_registration', methods=['POST','GET'])
def incident_registration():
    cname=request.form.get('cname')
    cgender=request.form.get('cgender')
    cdob=request.form.get('cdob')
    caddress=request.form.get('caddress')
    ccontactno=request.form.get('ccontact')
    cemail=request.form.get('cemail')
    Subject=request.form.get('Subject')
    date_of_occurance=request.form.get('date_of_occurance')
    place_of_occurance=request.form.get('place_of_occurance')
    description=request.form.get('description')
    myuser_id=dbs.incident_registration(cname, cgender, cdob, caddress, ccontactno, cemail, Subject, date_of_occurance, place_of_occurance, description)
    session['user_id']=myuser_id
    return redirect('/dashboard')
    
if __name__=="__main__":
    app.run(debug=True)