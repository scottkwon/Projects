from flask import Flask,render_template,request,redirect,session, flash
import re

app = Flask(__name__)
app.secret_key = "r348uq2djm4q2308rd207cmy2450"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r"^[a-zA-Z-']+$")
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')


def Validation():
    errors = 0

    #check fname
    if request.form['firstName'] == '':
        flash("Please enter your first name", 'firstNameError')
        errors += 1
    elif any(char.isdigit() for char in request.form['firstName']) == True:
        flash("Your first name cannot contain numbers", 'firstNameError')
        errors += 1
    else:
        session['firstName'] = request.form['firstName']

    #check lname
    if request.form['lastName'] == '':
        flash('Please enter your last name', 'lastNameError')
        errors += 1
    elif any(char.isdigit() for char in request.form['lastName']) == True:
        flash('Your last name cannot contain numbers', 'lastNameError')
        errors += 1
    else:
        session['lastName'] = request.form['lastName']

    #check email
    if request.form['email'] == '':
        flash('Please enter your email', 'emailError')
        errors += 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Enter a valid email', 'emailError')
        errors += 1
    else:
        session['email'] = request.form['email']

    #check password
    if request.form['pass'] == '':
        flash('Please enter your secret password', 'passwordError')
        errors += 1
    elif len(request.form['pass']) < 8:
        flash('Your password must have a minimum of 8 characters!', 'passwordError')
        errors += 1
    elif not PASSWORD_REGEX.match(request.form['pass']):
        flash('Please have atleast one uppercase and one number in your password', 'passwordError')
        errors += 1
    else:
        session['pass'] = request.form['pass']

    #check confpassword
    if request.form['confpass'] == '':
        flash('Please confirm your password', 'passwordError')
        errors += 1
    elif request.form['confpass'] != request.form['pass']:
        flash('Password did not match', 'passwordError')
        errors += 1
    else:
        session['pass'] = request.form['confpass']

    #checking for errors
    if errors > 0:
        return False
    else:
        return True

@app.route('/')
def Home():
    #if nothing stored, set to empty
    if 'firstName' not in session:
        session['firstName'] = ''
    if 'lastName' not in session:
        session['lastName'] = ''
    if 'email' not in session:
        session['email'] = ''
    if 'pass' not in session:
        session['pass'] = ''
    if 'confpass' not in session:
        session['confpass'] = ''
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def Create_User():
    if Validation() == False:
    #checks all conditions and redirect to home if any are not met
        return redirect('/')
    #redirect to new page with your input results
    return redirect('/process')


@app.route('/process')
def show_user():
    return render_template('process.html', firstName=session['firstName'], lastName=session['lastName'], email=session['email'])

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
