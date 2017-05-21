# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'survey_app/index.html')

def process(request):
    request.session['count'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result/')

def result(request):
    msg = 'Thanks for submitting this form! You have submitted this form {} times now!'.format(request.session['count'])
    messages.add_message(request, messages.INFO, msg)
    return render(request, 'survey_app/result.html')
