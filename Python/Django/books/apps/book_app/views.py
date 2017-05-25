# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Book
# Create your views here.
def index(request):
    context = {
    'Books': Book.objects.all()
    }
    return render(request, 'book_app/index.html', context)

def add(request):
    if request.method == 'POST':
        Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')
