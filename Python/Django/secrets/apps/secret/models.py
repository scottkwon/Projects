from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def check_registration(self, data):
        errors =[];
        if len(data['first_name']) < 2:
            errors.append('First Name must contain atleast 2 characters')
        if len(data['last_name']) < 2:
            errors.append('Last Name must contain atleast 2 characters')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('Please enter a valid email')
        if len(data['password']) < 8:
            errors.append('Password must be greater than 8 characters')
        check_user = self.filter(email=data['email'])
        if check_user:
            errors.append('Email has already been registered')
        if data['password'] != data['confirm_password']:
            errors.append('Password and password confirmation fields did not match')
        return errors

    def create_user(self, data):
        return self.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()))


    def verify_login(self, data):
        errors = [];
        if not EMAIL_REGEX.match(data['email']):
            errors.append('Invalid email format')
        if len(data['password']) == 0:
            errors.append('Please enter your password')
        check_user = User.objects.filter(email = data['email'])
        if check_user:
            hashed_pw = bcrypt.hashpw(data['password'].encode(), check_user[0].password.encode())
            if check_user[0].password == hashed_pw:
                pass
            else:
                errors.append('Username and Password do not match')
        else:
            errors.append('Email not found')
        return errors

class SecretManager(models.Manager):
    def validate(self, data):
        errors = []
        if len(data['content']) < 2:
            errors.append('Please enter a real secret')
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Secret(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name='secrets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SecretManager()

class Like(models.Model):
    user = models.ForeignKey(User, related_name='user_likes')
    secret = models.ForeignKey(Secret, related_name='secret_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

