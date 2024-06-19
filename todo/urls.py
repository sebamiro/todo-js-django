from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('finishTodo/<todo_id>', views.finishTodo, name='finishTodo'),
        path('deleteTodo/<todo_id>', views.deleteTodo, name='deleteTodo'),
        path('updateTodo/<todo_id>', views.updateTodo, name='updateTodo'),
]
