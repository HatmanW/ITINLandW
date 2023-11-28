from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    # Handling the form submission for adding new tasks
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    # Categorizing tasks based on importance and urgency
    tasks = Task.objects.all()
    do_now = tasks.filter(important=True, urgent=True)
    schedule = tasks.filter(important=True, urgent=False)
    delegate = tasks.filter(important=False, urgent=True)
    limit = tasks.filter(important=False, urgent=False)

    context = {
        'form': form,
        'do_now': do_now,
        'schedule': schedule,
        'delegate': delegate,
        'limit': limit,
    }
    return render(request, 'taskMgmt/task_list.html', context)
''' old task list
def task_list(request):
    tasks = Task.objects.all()

    do_now = tasks.filter(important=True, urgent=True)
    schedule = tasks.filter(important=True, urgent=False)
    delegate = tasks.filter(important=False, urgent=True)
    limit = tasks.filter(important=False, urgent=False)

    context = {
        'do_now': do_now,
        'schedule': schedule,
        'delegate': delegate,
        'limit': limit,
    }
    return render(request, 'taskMgmt/task_list.html', context)
'''

'''    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    return render(request, 'taskMgmt/task_list.html', {'tasks': tasks, 'form': form})'''

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'taskMgmt/add_task.html', {'form': form})

def mark_complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'taskMgmt/task_detail.html', {'task': task})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'taskMgmt/edit_task.html', {'form': form})