from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Task

def index(request):
    task_list = Task.objects.all()
     # Pagination with three tasks per page
    paginator = Paginator(task_list, 3)
    page_number = request.GET.get('page', 1)
    # try:
    #     tasks = paginator.page(page_number)
    #     print(tasks)
    # except PageNotAnInteger:
    #     # If page_number is not an integer, then deliver the first page
    #     tasks = paginator.page(1)
    # except EmptyPage:
    #     # If page_number  is out of range, then deliver last page of results
    #     tasks = paginator.page(paginator.num_pages)

    tasks = paginator.page(page_number)
    print(tasks)

    return render(request, "tasks/task/list.html", {'tasks': tasks})

# Create your views here.
