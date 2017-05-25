from django.shortcuts import render,redirect
from .models import course


def index(request):
    context = {
    'courses': course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def add(request):
    if request.method == 'POST':
        course.objects.create(name=request.POST['name'], description=request.POST['description'])
        print course
    return redirect('/')

def remove(request, id):
    context = {
    'target': course.objects.get(id=id)
    }
    print context
    return render(request, 'courses_app/remove.html', context)

def confirm(request,id):
    course.objects.get(id=id).delete()
    return redirect('/')
