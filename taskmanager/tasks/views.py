from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, get_object_or_404,redirect
from .forms import TaskForm

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer    

def task_list(request):
    tasks = Task.objects.all()
    return render (request,"tasks/task_list.html",{"tasks":tasks}) 

def task_detail(request,pk):
    task = get_object_or_404(Task,pk=pk)
    return render(request,"tasks/task_detail.html",{"task":task})  

def add_task(request):
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form=TaskForm()
    return render(request,"tasks/add_task.html",{"form":form})         


