from __future__ import unicode_literals

from django.db import models
import re
from django.contrib import messages

WORD_REGEX = re.compile(r"^[a-zA-Z0-9-:'\s]{2,}$")

# Create your models here.


class BookManager(models.Manager):

    def book_validation(self,request):
        no_errors = True

        if not WORD_REGEX.match(request.POST['title']):
            no_errors = False
            messages.error(request, 'Not a valid title')

        if request.POST['author_list'] ==  "None" and request.POST['new_author'] == "":
            no_errors = False
            messages.error(request, 'Please enter an author')

        if not WORD_REGEX.match(request.POST['content']):
            no_errors = False
            messages.error(request,'Please enter a thoughtful review')

        return no_errors


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey('login_app.User')
    book = models.ForeignKey(Book)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
