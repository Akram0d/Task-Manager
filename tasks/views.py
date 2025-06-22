from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
from django.shortcuts import get_object_or_404

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
