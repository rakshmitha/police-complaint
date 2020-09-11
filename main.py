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
        return render_template('dashboard.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

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

if __name__=="__main__":
    app.run(debug=True)