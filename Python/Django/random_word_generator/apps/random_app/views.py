# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'random' not in request.session:
        request.session['random'] = get_random_string(14)
    if 'count' not in request.session:
        request.session['count'] = 1
    return render(request, 'random_app/index.html')

def generate(request):
    request.session['random'] = get_random_string(14)
    request.session['count'] += 1
    return redirect ('/')
