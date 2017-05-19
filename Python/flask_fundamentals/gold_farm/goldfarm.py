from flask import Flask, redirect, request, render_template, session
import random, datetime

app = Flask(__name__)
app.secret_key = '24mnuq24589ycw347mt53890c5vty6452'


def randomnum(start, end):
    num = random.randrange(start,end)
    return num

def WorL():
    chance = random.randrange(0,2)
    if chance == 1:
        return True
    if chance == 0:
        return False

def addactivity(num, action, location):
    time = datetime.now()
    win = 'Earned {} from the {}! {}'.format(num, location, time)
    lost = 'Lost {} from the {}! {}'.format(num, location, time)
    if location == "farm":
        session['activity'].append(('earn', win))
    elif location == "cave":
        session['activity'].append(('earn', win))
    elif location == "house":
        session['activity'].append(('earn', win))
    elif location == "casino":
        if action == 'Earned':
            session['activity'].append(('earn', win))
        elif action == 'Lost':
            session['activity'].append(('lose', lost))
        else:
            print "error"
    else:
        print "error"

@app.route('/')
def home():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html', total=session['gold'], activity=session['activity'])

@app.route('/process_money', methods=['POST'])
def money():
    building = request.form['building']
    if building == "farm":
        farmgold = randomnum(10,21)
        session['gold'] += farmgold
        addactivity(farmgold, 'Earned', 'farm')
    elif building == "cave":
        cavegold = randomnum(5,11)
        session['gold'] += cavegold
        addactivity(cavegold, 'Earned', 'cave')
    elif building == "house":
        housegold = randomnum(2,6)
        session['gold'] += housegold
        addactivity(housegold, 'Earned', 'house')
    elif building == "casino":
        casinogold = randomnum(0,51)
        chance = WorL()
        if chance == True:
            session['gold'] += casinogold
            addactivity(casinogold, 'Earned', 'casino')
        elif chance == False:
            session['gold'] -= casinogold
            addactivity(casinogold, 'Lost', 'casino')
        else:
            print "error"
    else:
        print "error"
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.reset()
    return redirect('/')

app.run(debug=True)
