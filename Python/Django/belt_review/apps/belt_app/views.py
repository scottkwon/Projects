# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from .models import Review, Book, Author
from ..login_app.models import User
# Create your views here.
    # url(r'^books/$', views.dashboard, name='dashboard'),
    # url(r'^books/add/$', views.create_page, name='create_page'),
    # url(r'^books/create_book/$', views.create_book, name='create_book'),
    # url(r'^books/(?P<id>\d+)/$', views.book_review, name='book_review'),
    # url(r'^books/create_review/$', views.create_review, name='create_review'),
    # url(r'^users/(?P<id>\d+)/$', views.user_page, name='user_page'),
    # url(r'^logout/$', views.logout, name='logout'),


def dashboard(request):
    print request.session['user_id']
    return render(request, 'belt_app/dashboard.html')

def add_page(request):
    context = {
    'authors': Author.objects.all(),
    }
    return render(request, 'belt_app/add.html', context)

def create_book(request):
    if request.method == 'POST':
        if Book.objects.book_validation(request) == False:
            return redirect(reverse('books_app:add_page'))
        else:
            pass

        author_list = request.POST['author_list']
        author_input = request.POST['new_author']
        rating = request.POST['rating']
        content = request.POST['content']
        title = request.POST['title']
        user = User.objects.get(pk=request.session['user_id'])

        if author_list == 'None':
            current_author = request.POST['new_author']
        else:
            current_author = author_list

        try:
            book_author = Author.objects.filter(name=author_input)
            if book_author:
                messages.error(request,'Author already exists! Choose from the list')
        except:
            book_author = Author.objects.create(name=current_author)
            messages.success(request,'Author succesfully added!')

        book_check = Book.objects.filter(author__name=current_author, title=title)

        if book_check:
            add_review = Review.objects.create(content=content, rating=rating, user=user, book=book_check[0])

            return redirect('/books/{}/'.format(book_check[0].id))

        else:
            new_book = Book.objects.create(title=title, author=current_author)

            add_review = Review.objects.create(content=content, rating=rating, user=user, book=new.book)

            return redirect('/books/{}/'.format(new_book.id))

    return redirect('/books/add/')

def book_review(request, id):
    context = {
        'books': Book.objects.filter(id=id),
        'reviews': Review.objects.filter(book__id=id).order_by('-created_at')[:3],
    }
    return render(request, 'belt_app/book_review.html', context)

def create_review(request):
    pass

def user_page(request, id):
    pass

def logout(request):
    request.session.flush()
    return redirect('/')
