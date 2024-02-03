from django.urls import path
from .views import TaskView, TaskDetailView

urlpatterns= [
    path('', TaskView.as_view(), name = 'Task'), 
    path('task/<int:pk>/', TaskDetailView.as_view(), name = 'task'),
]