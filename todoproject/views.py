from django.http import HttpResponse
from django.shortcuts import render
from todoapp.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')   # '-updated_at' give data in desc order and 'updated_at' will give in asce ordr 
    completed_tasks = Task.objects.filter(is_completed = True)
    context = {
        'tasks': tasks,
        'completed_tasks':completed_tasks
    }
    return render(request,'home.html',context)

