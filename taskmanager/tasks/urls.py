from django.urls import path
from .views import TaskListCreateView, TaskDetailView, task_list

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name="task-list"),
    path('tasks/<int:pk>/',TaskDetailView.as_view(),name="task_detail"),
    path('',task_list,name='task_list')
]