# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]