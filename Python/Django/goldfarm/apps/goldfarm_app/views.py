# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import datetime, random

def randomnum(start,end):
    num = random.randrange(start,end)
    return num

def activity(request, num, action, location):
    time = datetime.datetime.now()
    win = 'Earned {} from the {}! {}'.format(num, location, time)
    lost = 'Lost {} from the {}! {}'.format(num, location, time)
    activity = request.session['activities']
    if request.session.get('activities', None):
        request.session['activities'] = []
    print activity
    if request.POST['building'] == "farm":
        activity.append(('earn', win))
    elif request.POST['building'] == "cave":
        activity.append(('earn', win))
    elif request.POST['building'] == "house":
        activity.append(('earn', win))
    elif request.POST['building'] == "casino":
        if action == 'Earned':
            activity.append(('earn', win))
        elif action == 'Lost':
            activity.append(('lose', lost))
    else:
        print "error"
    request.session['activities'] = activity


def WorL():
    chance = random.randrange(0,2)
    if chance == 1:
        return True
    if chance == 0:
        return False

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if not request.session.get('activities', None):
        request.session['activities'] = []
    context = {
        'total': request.session['gold'],
        'activities': request.session['activities']
    }
    return render(request, 'goldfarm_app/index.html', context)


def process_money(request):
    building = request.POST['building']
    if building == "farm":
        farmgold = randomnum(10,21)
        request.session['gold'] += farmgold
        activity(request, farmgold, 'Earned', 'Farm')
    if building == "cave":
        cavegold = randomnum(5,11)
        request.session['gold'] += cavegold
        activity(request, cavegold, 'Earned', 'Cave')
    if building == "house":
        housegold = randomnum(2,6)
        request.session['gold'] += housegold
        activity(request, housegold, 'Earned', 'House')
    if building == "casino":
        casinogold = randomnum(0,51)
        chance = WorL()
        if chance == True:
            request.session['gold'] += casinogold
            activity(request, casinogold, 'Earned', 'Casino')
        elif chance == False:
            request.session['gold'] -= casinogold
            activity(request, casinogold, 'Lost', 'Casino')
    else:
        print "error"
    return redirect('/')

def reset(request):
    del request.session['activities']
    del request.session['gold']
    return redirect('/')
