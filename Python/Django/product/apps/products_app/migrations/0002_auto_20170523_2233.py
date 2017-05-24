# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='desc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]