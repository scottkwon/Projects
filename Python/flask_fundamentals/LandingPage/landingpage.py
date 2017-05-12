from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')  #methods=["POST"] giving me 405 error method not accept
def dojo():
    #name = request.form['name']
    #email = request.form['email']
    return render_template('dojos.html')


app.run(debug=True)