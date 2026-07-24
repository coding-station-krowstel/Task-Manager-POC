from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer    

def task_list(request):
    tasks = Task.objects.all()
    return render (request,"tasks/task_list.html",{"tasks":tasks})    


