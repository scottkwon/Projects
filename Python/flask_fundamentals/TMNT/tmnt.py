from flask import Flask,render_template,request, redirect

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/<color>')
def Color(color):
    if color.lower() == "blue":
        src='img/Leonardo.jpg'
    elif color.lower() == "orange":
        src='img/Michelangelo.jpg'
    elif color.lower() == "red":
        src='img/Raphael.jpg'
    elif color.lower() == "purple":
        src='img/Donatello.jpg'
    return render_template('ninja.html', src=src)

app.run(debug=True)