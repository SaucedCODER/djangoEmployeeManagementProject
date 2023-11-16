from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from django.contrib import messages

# Create your views here.
def openAttendance(request):
    open_attendance_dates = Attendance.objects.filter(is_open=True)
 
    return render(request,'openAttendance.html',{'open': open_attendance_dates})

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
            messages.error(request, "You Must Be Logged In...")
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
        messages.success(request, "You Must Be Logged In...")
        return redirect('core:login')
def delete_appointment(request, pk):
    if request.user.is_authenticated:
        delete_it = Appointment.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Appointment Deleted Successfully...")
        return redirect('employees:appointment_list')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('employees:appointment_list')
    
def view_appointment(request, pk):
    pass
