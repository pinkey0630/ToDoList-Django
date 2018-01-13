#coding:utf-8
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from models import Todo
import datetime

def index(request):
    message = "当前时间:{}".format(datetime.datetime.now())
    return HttpResponse(message)
#class Todo:
    #def __init__(self, description, isCompleted):
        #self.description = description
        #self.isCompleted = isCompleted

def todolist(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
        	title = request.POST.get('title')
        	Todo.objects.create(title=title)

    list = Todo.objects.all()
    return render(request, 'todolist.html', locals())

def complete(request, pk):
	todo_item = get_object_or_404(Todo, id=pk)
	todo_item.completed = True
	todo_item.save()
	return HttpResponseRedirect('/')

def delete(request, pk):
	todo = get_object_or_404(Todo, id=pk)
	todo.delete()
	return HttpResponseRedirect('/')

    #for value in range(0, 10):
        #list.append(Todo("lfkdsk" + str(value), False))

