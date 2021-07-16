from django.shortcuts import render, redirect
from.models import Course
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    errors = Course.objects.course_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        Course.objects.create(
            name = request.POST['name'],
            description = request.POST['description']
        )
        return redirect('/')

def check(request, id):
    context = {
        'this_course' : Course.objects.get(id=id)
    }
    return render(request, 'check.html', context)

def delete(request, id):
    this_id = Course.objects.get(id=id)
    this_id.delete()
    return redirect('/')