# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request, 'landscapes_app/index.html')

def landscape(request, num):
    number = int(num)
    if number < 11:
        src='landscapes_app/img/snow.gif'
    elif number < 21:
        src='landscapes_app/img/desert.gif'
    elif number < 31:
        src='landscapes_app/img/forest.gif'
    elif number < 41:
        src='landscapes_app/img/vineyard.png'
    elif number < 51:
        src ='landscapes_app/img/tropical.gif'

    context = {
        'landscape': src
    }

    print src
    print num
    return render(request, 'landscapes_app/landscape.html', context)
