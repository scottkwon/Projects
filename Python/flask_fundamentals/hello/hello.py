from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name="Scott")

@app.route('/success')
def success():
    return render_template('success.html', name="Scott")

app.run(debug=True)


#output
#homepage
#Welcome to Flask
#localhost:50000/success
#You created another succesfull GET page!