from __future__ import unicode_literals

from django.db import models
import re
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def check_registration_form(self, request):
        no_error = True
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.error(request, 'Not a valid email!')
            no_error = False
        if len(request.POST['first_name']) < 2:
            messages.error(request, 'First name must be atleast 2 characters')
            no_error = False
        if len(request.POST['first_name']) > 16:
            messages.error(request,'First name cannot be more than 16 characters')
            no_error = False
        if len(request.POST['last_name']) < 2:
            messages.error(request,'Last name must be atleast 2 characters')
            no_error = False
        if len(request.POST['last_name']) > 16:
            messages.error(request,'Last name cannot be more than 16 characters')
            no_error = False
        if len(request.POST['password']) < 8:
            messages.error(request,'Password must be atleast 8 characters')
            no_error = False
        check_user = self.filter(email=request.POST['email'])
        if check_user:
            messages.error(request, 'Email already exists')
            no_error = False
        return no_error

    def verify_login(self, request):
        no_error = True
        if not EMAIL_REGEX.match(request.POST['email']):
            no_error=False
            messages.error(request, 'Email format not valid')
        target = User.objects.filter(email = request.POST['email'])
        if target:
            if request.POST['password'] == target[0].password:
                request.session['first_name'] = target[0].first_name
            else:
                no_error = False
                messages.error(request, 'Username and Password do not match')
        else:
            no_error=False
            messages.error(request, 'Email not found')
        return no_error



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
