# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio_app/index.html')

def blog(request):
    return render(request, 'portfolio_app/blog.html')

def about_me(request):
    return render(request, 'portfolio_app/about_me.html')

def projects(request):
    return render(request, 'portfolio_app/projects.html')
