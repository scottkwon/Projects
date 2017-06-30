from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):

    def check_user(self,data):
        returning_user = True
        user = User.objects.filter(name=data['name'])
        if user:
            pass
        else:
            returning_user = False
        return returning_user


class Interest(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    interests = models.ManyToManyField(Interest, related_name='Users')
    objects = UserManager()
