from flask import Flask,render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

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
    return "the email is {} and the pass is {}".format(email,password)

if __name__=="__main__":
    app.run(debug=True)