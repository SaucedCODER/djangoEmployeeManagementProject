from django.shortcuts import render, redirect
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