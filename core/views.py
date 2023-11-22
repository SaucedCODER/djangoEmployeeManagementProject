from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from projects.models import Task, Project
from employees.models import Attendance
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    user = request.user
    if request.user.is_authenticated:
        if user is not None and user.is_staff is True:
                logout(request, user)
                messages.success(request, "You Have Been Logged Out!")
                return redirect('core:login')
        # Get the total number of tasks
        total_tasks = Task.user_tasks(user)
        overdue_tasks = Task.overdue_tasks(user)
        completed_tasks = Task.completed_tasks(user)
        completed_projects = Project.completed_projects(user)
        present_days = Attendance.present_days_count(user)
        # Get the total number of projects
        total_projects = Project.assigned_projects(user)
        
        context = { 'total_projects': total_projects, 
                   'total_tasks': total_tasks,
                   'overdue_tasks': overdue_tasks,
                   'completed_tasks': completed_tasks,
                   'completed_projects': completed_projects,
                    'present_days' : present_days,
                   }
        
        return render(request,'core/home.html',context)
    return render(request,'core/login.html',{})

def login_user(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None and user.is_staff is False:
                login(request, user)
                messages.success(request, "You Have Been Logged In!")
                return redirect('core:home')
       elif user and user.is_staff is True:
                login(request, user)
                return redirect('core:admin')
       else:
          messages.error(request, "Wrong User Name Or Password") 
          return redirect('core:home')
    return render(request,'core/login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('core:home')

from core.models import Notification
from django.shortcuts import get_object_or_404
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    notification.is_read = True
    notification.save()
    messages.success(request, "Successfully Marked As Read...")
    return redirect('employees:appointment_list')


