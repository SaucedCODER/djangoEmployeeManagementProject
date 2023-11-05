from django.shortcuts import render
from django.db.models import Avg
from projects.models import Project
from projects.models import Task
from projects.forms import TaskCreationForm
from projects.forms import ProjectCreationForm
from django.contrib import messages


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(due='2')
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
    }
    return render(request, 'projects/projects.html', context)

def newTask(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
           
            context = {
                'form': form,
            }
            messages.success(request, "Congratulations, your Task was created!")
            return render(request, 'core/home.html', context)
        else:
            return render(request, 'projects/createtask.html', context)
    else:
        form = TaskCreationForm()
        context = {
            'form': form,
        }
        return render(request,'createtask.html', context)

def newProject(request):
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
           
            form = ProjectCreationForm()
            context = {
                'form': form,
            }
            messages.success(request, "Congratulations, your project was created!")
            return render(request, 'createproject.html', context)
        else:
            return render(request, 'createproject.html', context)
    else:
        form = ProjectCreationForm()
        context = {
            'form': form,
        }
        return render(request,'createproject.html', context)
