from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})


def toggle_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('home')


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')

