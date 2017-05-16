from flask import Flask,render_template,request,redirect,session, flash
import re

app = Flask(__name__)
app.secret_key = "r348uq2djm4q2308rd207cmy2450"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def submit():
    if len(request.form['name']) < 1:
        flash("Please enter your name!")
    else:
        flash("Succesfully entered name.")
    if len(request.form['comment']) < 1:
        flash("Please enter something about yourself!")
    elif len(request.form['comment']) > 121:
        flash('Too much information about yourself, please keep it under 120 characters!')
    else:
        flash("You have successfully submitted your information")
    return redirect('/')
def result():
    name = request.form['name']
    location = request.form['location']
    lang = request.form['lang']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, lang=lang, comment=comment)

app.run(debug=True)
