from django.shortcuts import render, redirect, HttpResponse
from .models import User,Interest

def index(request):
    return render(request, 'interests/index.html')

def add(request):
    if request.method == 'POST':
        data = request.POST.copy()
        user = User.objects.filter(name=data['name'].lower())
        if not user:
            new_user = User.objects.create(name = data['name'].lower())
            interest = Interest.objects.create(content = data['content'])
            new_user.interests.add(interest)
            return redirect('/users')
        else:
            existing_user = User.objects.filter(name = data['name'].lower())
            interest = Interest.objects.create(content = data['content'])
            existing_user[0].interests.add(interest)
            return redirect('/users')

def users(request):
    context = {
    'users': User.objects.all(),
    }
    return render(request, 'interests/users.html', context)

def show(request, id):
    context = {
    'user': User.objects.get(id=id),
    'interests': Interest.objects.filter(Users__id=id)
    }
    return render(request, 'interests/show.html', context)

def delete(request,id):
    Interest.objects.get(id=id).delete()
    return redirect('/users')
