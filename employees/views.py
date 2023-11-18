from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from django.contrib import messages
from itertools import chain
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def view_profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    return render(request, 'view_profile.html', {'user': user, 'user_profile': user_profile})

from employees.forms import UserProfileUpdateForm, CustomUserChangeForm, CustomPasswordChangeForm



@login_required
def update_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('employees:view_profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=user_profile)

    return render(request, 'update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
      
    })
from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the session to avoid the user being logged out
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('employees:view_profile')  # Change this to your actual profile view name
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})

def openAttendance(request):
    user = request.user
    if user.is_authenticated:
        open_attendance_dates = Attendance.objects.filter(is_open=True)
        # Get all 'present' attendance records for the user
        present_attendances = Attendance.objects.filter(user=user, status='present')
        # Get all 'not_set' attendance records for the user
        not_set_attendances = Attendance.objects.filter(user=user, status='not_set')

        # Concatenate 'present' and 'not_set' attendance records into a single array
        all_attendances = list(chain(present_attendances, not_set_attendances))
        return render(request,'openAttendance.html',{
        'open': open_attendance_dates,
        'all_attendances': all_attendances
        })
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('core:login')

def setAttendance(request, date):
    user = request.user  
    if user.is_authenticated:
        result = Attendance.mark_attendance(user=user, date=date)
        if result:
            messages.success(request, "Attendance has been marked as Present...")
        else:
            messages.error(request, "You have already marked attendance for this date...")
        return redirect('core:home')
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('core:login')
    
# employees/views.py
from .models import Appointment
from .forms import AppointmentForm, AppointmentFilterForm

def create_appointment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                appointment = form.save(commit=False)
                appointment.user = request.user
                appointment.save()
                return redirect('employees:appointment_list')
        else:
            form = AppointmentForm()
        return render(request, 'create_appointment.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In To Do That...")
        return redirect('core:login')

def appointment_list(request):
    if request.user.is_authenticated:    
        appointments = Appointment.objects.filter(user=request.user)
        filter_form = AppointmentFilterForm(request.GET)
        if filter_form.is_valid():
            status = filter_form.cleaned_data.get('status')
            if status:
                appointments = appointments.filter(status=status)
        return render(request, 'appointment_list.html', {'appointments': appointments, 'filter_form': filter_form})
    else:
            messages.error(request, "You Must Be Logged In To View That Page...")
            return redirect('core:login')
def update_appointment(request, pk):
    if request.user.is_authenticated:
        appointment = get_object_or_404(Appointment, id=pk)
        if request.method == 'POST':
            form = AppointmentForm(request.POST, instance=appointment)
            print(form)
            if form.is_valid():
                
                form.save()
                messages.success(request, "Appointment Has Been Updated!")
                return redirect('employees:appointment_list')
        else:  
            form = AppointmentForm(instance=appointment)
        return render(request, 'update_appointment.html', {'form': form})

    else:
        messages.error(request, "You Must Be Logged In To Do That...")
        return redirect('core:login')
def delete_appointment(request, pk):
    if request.user.is_authenticated:
        delete_it = Appointment.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Appointment Deleted Successfully...")
        return redirect('employees:appointment_list')
    else:
        messages.error(request, "You Must Be Logged In To Do That...")
        return redirect('employees:appointment_list')
    
def view_appointment(request, pk):
    if request.user.is_authenticated:
        print(pk)
        # Look Up tasks and project information
        data = Appointment.objects.get(id = pk)
        return render(request, 'view_appointment.html', {'appointment':data})
    else:
        messages.error(request, "You Must Be Logged In To View That Page...")
        return redirect('core:login')
