from django.urls import path
from . import views
from .views import TodoList

urlpatterns = [
    path('', views.index, name='index'),
    path('todo', TodoList.as_view(), name='list')
]