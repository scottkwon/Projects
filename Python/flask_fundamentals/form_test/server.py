from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    print "Got Post Info"
    print request.form
    return redirect('/')

@app.route('/show')
def show_users():
    return render_template('user.html', name="Scott", email='scottykwon@gmail.com')

@app.route('/users/<username>')
def show_user_profile(username):
    return render_template("user.html", name = username)

app.run(debug=True)