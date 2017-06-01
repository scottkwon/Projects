from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages, sessions
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def process(request):
    if request.method == 'POST':
        no_errors = User.objects.check_registration_form(request)
        if no_errors == False:
            return redirect('/')
        else:
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
            messages.success(request,'Thank you for registering!')
            user = User.objects.get(email=request.POST['email'])
            request.session['first_name'] = user.first_name
            request.session['user_id'] = user.id
            return redirect('/books/')

def login(request):
    if request.method == 'POST':
        no_validation_error = User.objects.verify_login(request)
        user = User.objects.get(email=request.POST['email'])
        if no_validation_error == True:
            request.session['first_name'] = user.first_name
            request.session['user_id'] = user.id
            return redirect('/books/')
        else:
            return redirect('/')

def success(request):
    messages.success(request, 'You have successfully logged in!')
    context = {
    'users': User.objects.all()
    }
    return render(request, '/books/', context)
