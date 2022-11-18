from django.shortcuts import render
from .models import Task

def index(request):
    task_list = Task.objects.all()
    return render(request, "tasks/task/list.html", {'task_list': task_list})

# Create your views here.
