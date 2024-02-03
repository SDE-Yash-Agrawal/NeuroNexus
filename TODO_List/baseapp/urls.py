from django.urls import path
from .views import TaskView, TaskDetailView, TaskCreate, TaskUpdate

urlpatterns= [
    path('', TaskView.as_view(), name = 'Task'), 
    path('task/<int:pk>/', TaskDetailView.as_view(), name = 'task'),
    path('task-create/', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
]