from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)



#homepage output:
#Hello visitor, my name is Scott Kwon. Welcome to my portfolio page!

#projects output:
#My projects:
#Fully Functional Original #151 Pokemon Pokedex
#Weather App
#Site Mockups