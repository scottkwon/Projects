from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'login')

@app.route('/')
def index():
    query = "SELECT first_name, last_name, age, DATE_FORMAT(created_at, '%m/%d/%Y') as date FROM friends"
    friends = mysql.query_db(query)
    query_date = "SELECT DATE_FORMAT(created_at, '%m/%d/%Y') as date FROM friendsdb.friends"
    dates = mysql.query_db(query_date)
    return render_template('index.html', all_friends=friends, dates=dates)

@app.route('/friends/<friend_id>')
def show(friend_id):
    query = " SELECT * FROM friends WHERE id=:specific id"
    data = {
    'specific_id': friend_id
    }
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0])

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends(first_name, last_name, created_at, age) VALUES (:first_name, :last_name, NOW(), :age)"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    mysql.query_db(query,data)
    return redirect('/')

app.run(debug=True)
