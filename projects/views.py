from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Avg
from projects.models import Project
from projects.models import Task
from projects.forms import TaskCreationForm
from projects.forms import ProjectCreationForm
from django.contrib import messages
from datetime import datetime


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(due='2')
    current_date = datetime.now()
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
        'current_date': current_date
        
    }
    return render(request, 'projects.html', context)

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
            return render(request, 'createtask.html', context)
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
    
def viewProject(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        project = Project.objects.get(id=pk)
        return render(request, 'manageproject.html', {'project':project})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('core:login')
def deleteProject(request, pk):
    pass
def updateProject(request, pk):
    if request.user.is_authenticated:
        project = Project.objects.get(id=pk)
        form = ProjectCreationForm(request.POST or None, instance=project)
        
        if form.is_valid():        
            form.save()
            next = request.POST.get('next', '/')
            print(next)
            messages.success(request, "Project Has Been Updated!")
            return HttpResponseRedirect(next)
        else:
            return_url = request.GET.get('return_url', '/')
            return render(request, 'updateproject.html', {'form':form,'return_url':return_url})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('core:login')
    
    # def update_record(request, pk):
	# if request.user.is_authenticated:
	# 	current_record = Record.objects.get(id=pk)
	# 	form = AddRecordForm(request.POST or None, instance=current_record)
	# 	if form.is_valid():
	# 		form.save()
	# 		messages.success(request, "Record Has Been Updated!")
	# 		return redirect('home')
	# 	return render(request, 'update_record.html', {'form':form})
	# else:
	# 	messages.success(request, "You Must Be Logged In...")
	# 	return redirect('home')
