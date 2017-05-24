# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Book
# Create your views here.
def index(request):
    Book.objects.create(title='Harry Potter', author='J.K Rowling', published_year='2001')
    Book.objects.create(title='Coraline', author='Neil Gaiman', published_year='2002')
    Book.objects.create(title='Fangirl', author='Rainbow Rowell', published_year='2013')
    Book.objects.create(title='The Help', author='Kathryn Stockett', published_year='2009')
    Book.objects.create(title='The Hobbit', author='J.R.R Tolkien', published_year='1937')
    books = Book.objects.all()
    for book in books:
        print book.title, book.author, book.published_year
    return HttpResponse('book_app/index.html')
