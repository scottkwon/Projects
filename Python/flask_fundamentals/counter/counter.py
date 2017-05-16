from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'awofj3i2u2wrwofnwaojti4ojtnf'


@app.route('/')
def index():
    session['count'] = 0
    return render_template('index.html', count=session['count'])

@app.route('/plus1')
def plus1():
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/plus2')
def plus2():
    session['count'] += 2
    return render_template('index.html', count=session['count'])

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)