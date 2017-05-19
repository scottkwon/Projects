from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = '1eu2rh24rh49fwfhw9'

@app.route('/')
def index():
    session['snum'] = random.randrange(1,11)
    print session['snum']
    return render_template('index.html')

@app.route('/posted', methods=['POST'])
def posted():
    if request.form['number_guessed'].isdigit():
        if int(request.form['number_guessed']) > session['snum']:
            return render_template('index.html', clue="Too high!", col="red", hide="hide")
    if request.form['number_guessed'].isdigit():
        if int(request.form['number_guessed']) < session['snum']:
            return render_template('index.html', clue="Too low!", col="red", hide="hide")
    if request.form['number_guessed'].isdigit():
        if int(request.form['number_guessed']) == session['snum']:
            return render_template('index.html', clue="{} was the number!".format(session['snum']), col="green", hide="")

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
