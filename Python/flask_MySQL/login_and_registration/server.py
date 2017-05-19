from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
from hashlib import md5
import os,binascii

app = Flask(__name__)
mysql = MySQLConnector(app,'login')
app.secret_key = "r348uq2djm4q2308rd207cmy2450"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r"^[a-zA-Z-']+$")
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
salt = binascii.b2a_hex(os.urandom(15))

def Validate_Email():
    errors = 0
    if request.form['email'] == '':
        flash('Please enter your email', 'emailError')
        errors += 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Enter a valid email', 'emailError')
        errors += 1
    else:
        session['email'] = request.form['email']
    if errors > 0:
        return False
    else:
        return True


def Validation():
    errors = 0
    #check fname
    if request.form['first_name'] == '':
        flash("Please enter your first name", 'firstNameError')
        errors += 1
    elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash("Your first name cannot contain numbers", 'firstNameError')
        errors += 1
    else:
        session['first_name'] = request.form['first_name']


    #check lname
    if request.form['last_name'] == '':
        flash('Please enter your last name', 'lastNameError')
        errors += 1
    elif any(char.isdigit() for char in request.form['last_name']) == True:
        flash('Your last name cannot contain numbers', 'lastNameError')
        errors += 1
    else:
        session['last_name'] = request.form['last_name']

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
    if request.form['password'] == '':
        flash('Please enter your secret password', 'passwordError')
        errors += 1
    elif len(request.form['password']) < 8:
        flash('Your password must have a minimum of 8 characters!', 'passwordError')
        errors += 1
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash('Please have atleast one uppercase and one number in your password', 'passwordError')
        errors += 1
    else:
        session['password'] = request.form['password']

    #check confpassword
    if request.form['confirm_password'] == '':
        flash('Please confirm your password', 'passwordError')
        errors += 1
    elif request.form['confirm_password'] != request.form['password']:
        flash('Password did not match', 'passwordError')
        errors += 1

    #checking for errors
    if errors > 0:
        return False
    else:
        return True

@app.route('/')
def Log_in():
    return render_template('log_in.html')

@app.route('/check', methods=['POST'])
def Valid():
    if Validate_Email() == True:
        query_email = "SELECT * FROM users WHERE email = :email"
        data = {
        'email': request.form['email']
        }
        checks = mysql.query_db(query_email, data)
        if len(checks) > 0:
            for check in checks:
                if check['email'] == request.form['email']:
                    if md5(request.form['password'] + check['salt']).hexdigest() == check['hashed_password']:
                        return redirect('/success')
                    else:
                        flash('Email and Password combination you entered did not match our files!', 'inputError')
                        return redirect('/')
                else:
                    flash('Please register a username and password!', 'inputError')
                    return redirect('/register')
        else:
            return redirect('/register')
    else:
        return redirect('/')

@app.route('/register')
def Register():
    return render_template('register.html')

@app.route('/add_user', methods=['POST'])
def Add_User():
    if Validation() == True:
        query_add = 'INSERT INTO users (first_name, last_name, email, salt, hashed_password, created_at, updated_at) VALUES (:first_name,:last_name, :email, :salt, :hashed_password, now(), now())'
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'salt': salt,
            'hashed_password': md5(request.form['password'] + salt).hexdigest()
        }
        mysql.query_db(query_add, data)
        return redirect('/success')
    else:
        return redirect('/register')

@app.route('/success')
def Success():
    return render_template('success.html')


app.run(debug=True)
