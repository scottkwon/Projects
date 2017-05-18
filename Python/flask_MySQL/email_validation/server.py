from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'valid_emails')
app.secret_key = 'qijeqoihqwohrqu9rhq9rh39r8q'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Enter a valid email')
        return redirect('/')
    query_email = "SELECT * FROM emails WHERE email = :email"
    data = {
    'email': request.form['email']
    }
    mails = mysql.query_db(query_email, data)
    if mails:
        flash('Email Already Exists!')
        return redirect('/')
    else:
        query_add = 'INSERT INTO emails (email, created_at) VALUES (:email, now())'
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query_add, data)
        return redirect('/success')

@app.route('/success')
def success():
    flash("Congrats! You have entered an unique EMAIL address!")
    query_email = "SELECT email, created_at FROM emails"
    emails = mysql.query_db(query_email)
    return render_template('success.html', emails=emails)

app.run(debug=True)
