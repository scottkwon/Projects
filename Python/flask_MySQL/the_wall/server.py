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

    #check email
    if request.form['email'] == '':
        flash('Please enter your email', 'emailError')
        errors += 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Enter a valid email', 'emailError')
        errors += 1

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
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def Valid():
    if Validate_Email() == True:
        query_email = "SELECT * FROM users WHERE email = :email"
        data = {
        'email': request.form['email']
        }
        checks = mysql.query_db(query_email, data)
        if checks:
            if checks[0]['email'] == request.form['email']:
                if md5(request.form['password'] + checks[0]['salt']).hexdigest() == checks[0]['hashed_password']:
                    session['user_id'] = checks[0]['id']
                    session['user_name'] = checks[0]['first_name']
                    return redirect('/wall')
                else:
                    flash('Email and Password combination you entered did not match our files!', 'inputError')
                    return redirect('/')
            else:
                flash('Please register a username and password!', 'inputError')
                return redirect('/')
        else:
            return redirect('/')
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
        created_user_id = mysql.query_db(query_add, data)
        session['user_id'] = created_user_id[0]['id']
        session['user_name'] = created_user_id[0]['first_name']
        # query_string = 'SELECT * FROM users WHERE id=:my_id'
        # data = {
        # 'my_id': created_user_id
        # }
        # found_user = mysql.query_db(query_string, data)
        # session['user_id'] = checks[0]['id']
        # session['user_name'] = checks[0]['first_name']
        return redirect('/wall')
    else:
        return redirect('/register')

@app.route('/wall')
def wall():
    messages_query = "SELECT messages.id, users.first_name, users.last_name, messages.content, messages.created_at FROM messages JOIN users ON messages.user_id = users.id"
    all_messages = mysql.query_db(messages_query)
    for a_message in all_messages:
        comments_query = "SELECT comments.content, users.first_name, users.last_name, comments.created_at FROM comments JOIN users on comments.user_id = users.id WHERE comments.message_id = :msg_id"
        data = {
        'msg_id': a_message['id']
        }
        a_message['comments'] = mysql.query_db(comments_query, data)
    return render_template('wall.html', messages=all_messages)

@app.route('/messages', methods=['POST'])
def create_message():
    query_string = "INSERT INTO messages (content, user_id, created_at, updated_at) VALUES (:content, :user_id, NOW(), NOW())"
    data = {
    "content": request.form['content'],
    "user_id": session['user_id']
    }
    mysql.query_db(query_string,data)
    return redirect('/wall')

@app.route('/comments', methods=['POST'])
def create_comment():
    query_string = "INSERT INTO comments (content, user_id, message_id, created_at, updated_at) VALUES (:content, :user_id, :msg_id, NOW(), NOW())"
    data = {
    'user_id': session['user_id'],
    'msg_id': request.form['message_id'],
    'content': request.form['content']
    }
    mysql.query_db(query_string, data)
    return redirect ('/wall')
app.run(debug=True)
