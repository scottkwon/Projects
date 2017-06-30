# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from django.db.models import Count
from .models import Review, Book, Author
from ..login_app.models import User

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'reviews': Review.objects.all().order_by('-created_at')[:3],
        'more_reviews': Review.objects.all().order_by('-created_at')[3:]
    }
    return render(request, 'belt_app/dashboard.html', context)

def add_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
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
        current_author = ''
        rating = request.POST['rating']
        content = request.POST['content']
        title = request.POST['title']
        user = User.objects.get(pk=request.session['user_id'])

        if author_list == 'None':
            current_author = author_input
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
            author = Author.objects.create(name=current_author)

            new_book = Book.objects.create(title=title, author=author)

            add_review = Review.objects.create(content=content, rating=rating, user=user, book=new_book)

            return redirect('/books/{}/'.format(new_book.id))

    return redirect('/books/add/')

def book_review(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'book': Book.objects.get(id=id),
        'reviews': Review.objects.filter(book__id=id).order_by('-created_at'),
    }
    return render(request, 'belt_app/book_review.html', context)

def create_review(request,id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    Review.objects.create(content=request.POST['content'], rating=request.POST['rating'], user=user, book=book)
    messages.success(request, 'Review Successfully Added!')
    return redirect('/books/{}/'.format(book.id))

def user_page(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    user_reviews = Review.objects.filter(user__id=request.session['user_id'])
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'count': len(user_reviews),
        'books': Book.objects.filter(reviews__user__id=request.session['user_id'])
    }
    return render(request, 'belt_app/user.html', context)

def delete(request, id):
    if request.method == 'POST':
        context = {
            'delete': Review.objects.get(id=id).delete()
        }
    return redirect()

def logout(request):
    request.session.flush()
    return redirect('/')
