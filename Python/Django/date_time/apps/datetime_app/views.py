# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.utils.timezone import activate
import datetime, pytz
# Create your views here.

def index(request):
    date = datetime.datetime.now().date().strftime('%B %-d, %Y')
    time = datetime.datetime.now().time().strftime('%-I:%M %p')
    context = {
        "date": date,
        "time": time
    }
    return render(request, 'datetime_app/index.html', context)
