from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name="task-list"),
    path('tasks/<int:pk>/',views.TaskDetailView.as_view(),name="task_detail_api"),
    path('',views.task_list,name='task_list'),
    path("task/<int:pk>/",views.task_detail,name="task_detail"),
    path("task/add/",views.add_task,name="add_task")
]