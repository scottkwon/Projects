from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    print User.objects.all()
    return render(request, 'login_app/index.html')

def process(request):
    if request.method == 'POST':
        errors = User.objects.check_registration_form(request)
        if errors == False:
            return redirect('/')
        else:
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
            messages.success(request,'Thank you for registering!')
            # request.session['first_name'] = request.POST['first_name']
            return redirect('/success/')

def login(request):
    if request.method == 'POST':
        validation_error = User.objects.verify_login(request)
        if validation_error == True:
            return redirect('/success')
        else:
            return redirect('/')

def success(request):
    messages.success(request, 'You have successfully logged in!')
    context = {
    'users': User.objects.all()
    }
    return render(request, 'login_app/success.html', context)
