from django.shortcuts import render
from django.views.generic.list import  ListView
from .models import Task

class Task(ListView):
    model = Task