# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
import random


VALUES = ['scott', 'steven', 'anessa', 'amir', 'sara', 'ruben', 'isaac', 'phillip', 'niels', 'joel', 'andres']


# Create your views here.
def index(request):
    if surprises not in request.session:
        request.session['surprises'] = []
    return render(request, 'surprise_app/index.html')

def process(request):
    if request.POST['number'].isdigit() and request.POST['number'] > 0:
        number = int(request.POST['number'])
        for value in range(0,number):
            request.session['surprises'].append(random.choice(VALUES))
    else:
        messages.add_message(request, messages.INFO, 'Please enter a number greater than zero')
        return redirect('/')
    print request.session['surprises']
    request.session.modified = True
    return redirect('/surprises/')

def surprises(request):
    context = {
        'surprises': request.session['surprises'],
    }
    print context
    return render(request, 'surprise_app/surprises.html', context)

def reset(request):
    del request.session['surprises']
    return redirect('/')
