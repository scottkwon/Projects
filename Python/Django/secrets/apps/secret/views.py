from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Count
import bcrypt
import re
from .models import User, Secret, Like

# Create your views here.
def index(request):
    return render(request, 'secret/index.html')

def process(request):
    if request.method == 'POST':
        data = request.POST.copy()
        errors = User.objects.check_registration(data)
        if not errors:
            user1 = User.objects.create_user(data)
            request.session['user_id'] = user1.id
            request.session['first_name'] = user1.first_name
            return redirect('/secrets')
        for error in errors:
            messages.error(request, error)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        data = request.POST.copy()
        errors = User.objects.verify_login(data)
        if not errors:
            user = User.objects.get(email=data['email'])
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            return redirect('/secrets')
        for error in errors:
            messages.error(request,error)
    return redirect('/')

def secrets(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'secrets': Secret.objects.all().order_by('-created_at').annotate(num_likes=Count('secret_likes'))[:5],
        'my_likes':
        Secret.objects.filter(secret_likes__user=user)
    }

    return render(request,'secret/secrets.html', context)

def post(request):
    if request.method == 'POST':
        data = request.POST.copy()
        user = User.objects.get(id = request.session['user_id'])
        errors = Secret.objects.validate(data)
        if user:
            if not errors:
                Secret.objects.create(content = data['content'], user = user)
        else:
            redirect('/')
        for error in errors:
            messages.error(request,error)
    return redirect('/secrets/')

def delete(request, id):
    Secret.objects.get(id=id).delete()
    return redirect('/secrets')

def like(request, id):
    user = User.objects.get(id=request.session['user_id'])
    secret = Secret.objects.get(id=id)
    Like.objects.create(user = user, secret = secret)
    origin = request.META['HTTP_REFERER']
    page = origin.split('/')[3]
    return redirect(reverse('secret:'+page))
    
def user(request):

    context = {
        'user_activities`': Secret.objects.filter(user_likes__id=user, user=user),
        'user': User.objects.get(id=id)
    }
    return render(request, 'secret/user.html', context)

def popular(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
    'secrets': Secret.objects.all().annotate(num_likes=Count('secret_likes')).order_by('-num_likes'),
    'my_likes':
    Secret.objects.filter(secret_likes__user=user)
    }
    return render(request, 'secret/popular.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')
