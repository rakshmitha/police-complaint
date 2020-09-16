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
        return redirect('/dashboard')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        history=dbs.get_history(session['user_id'])
        print (history)
        return render_template('dashboard.html', history=history)
    else:
        return render_template('login.html')


@app.route('/login_validation', methods=['POST','GET'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    myuser_id=dbs.login(email, password)
    if myuser_id==-1:
        return render_template('login.html')   
    else:
        session['user_id']=myuser_id
        return redirect('/dashboard')

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
    return render_template('register_complaint.html')

@app.route('/incident_registration', methods=['POST','GET'])
def incident_registration():
    if 'user_id' in session:
        cname=request.form.get('cname')
        #cgender=request.form.get('cgender')
        #cdob=request.form.get('cdob')
        #caddress=request.form.get('caddress')
        ccontactno=request.form.get('ccontact')
        cemail=request.form.get('cemail')
        #Subject=request.form.get('Subject')
        #date_of_occurance=request.form.get('date_of_occurance')
        place_of_occurance=request.form.get('place_of_occurance')
        description=request.form.get('description')
        user_id=session['user_id']
        myuser_id=dbs.incident_registration(cname, ccontactno, cemail, place_of_occurance, description,user_id)
        #session['user_id']=myuser_id
        return redirect('/dashboard')
    else:
        return render_template('login.html')

@app.route('/contactus')
def contactus():
    if 'user_id' in session:
        return render_template('contactus.html')
    else:
        return render_template('login.html')

@app.route('/helpline')
def helpline():
    if 'user_id' in session:
        return render_template('helpline.html')
    else:
        return render_template('login.html')


@app.route('/view/<complaint_id>')
def view(complaint_id):
    if 'user_id' in session:
        complaint_details=dbs.get_complaint(complaint_id)
        return render_template('view.html', complaint_details=complaint_details)
    else:
        return render_template('login.html')


    
if __name__=="__main__":
    app.run(debug=True)