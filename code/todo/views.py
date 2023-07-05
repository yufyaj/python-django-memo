from django.shortcuts import render
from django.views.generic import ListView

from .models import Todo

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

class TodoList(ListView):
    model = Todo
    context_object_name = 'tasks'