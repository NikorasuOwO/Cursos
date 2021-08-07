from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):

    tasks = Task.objects.order_by('-created')

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')



    context = {'tasks':tasks, 'form':form}

    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):

    task = Task.objects.get(pk=pk)

    form = TaskForm(instance=task) # Form will be pre-filled with 'task' info

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()

        return redirect('list')


    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(pk=pk)


    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)