from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    todos = Todo.objects.all()
    context = {'todos': todos, 'form': form}

    return render(request, 'home.html', context)

def finishTodo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('home')

def deleteTodo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('home')

def updateTodo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
    return redirect('home')
