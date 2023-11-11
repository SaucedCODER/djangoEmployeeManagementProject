from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request,'core/home.html',{})
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
