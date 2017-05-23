# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tmnt_app/index.html')

def show(request, color):
    if color.lower() == "blue":
        src='tmnt_app/img/Leonardo.jpg'
    elif color.lower() == "orange":
        src='tmnt_app/img/Michelangelo.jpg'
    elif color.lower() == "red":
        src='tmnt_app/img/Raphael.jpg'
    elif color.lower() == "purple":
        src='tmnt_app/img/Donatello.jpg'
    context = {
        'color': src
    }
    return render(request, 'tmnt_app/show.html', context)
