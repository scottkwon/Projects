from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    lang = request.form['lang']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, lang=lang, comment=comment)

app.run(debug=True)