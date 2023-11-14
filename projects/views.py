from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Avg
from projects.models import Project
from projects.models import Task
from projects.forms import TaskCreationForm
from projects.forms import ProjectCreationForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.
def projects(request):
    projects = Project.objects.filter(assign = request.user.id)
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    # overdue_tasks = tasks.filter(end='2')
    current_date = datetime.now()
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        # 'overdue_tasks' : overdue_tasks,
        'current_date': current_date
        
    }
    return render(request, 'projects.html', context)

def viewProject(request, pk):
    if request.user.is_authenticated:
        # Look Up tasks and project information
        tasks = Task.objects.filter(project_id = pk)
        project = Project.objects.get(id=pk)
        return render(request, 'manageproject.html', {'project':project,'tasks':tasks})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('core:login')

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
    
def updateTask(request, pk):
    if request.user.is_authenticated:
        task = Task.objects.get(id=pk)
        form = TaskCreationForm(request.POST or None, instance=task)
        
        if form.is_valid():        
            form.save()
            next = request.POST.get('next', '/')
            print(next)
            messages.success(request, "Task Has Been Updated!")
            return HttpResponseRedirect(next)
        else:
            return_url = request.GET.get('return_url', '/')
            return render(request, 'updatetask.html', {'form':form,'return_url':return_url})
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
