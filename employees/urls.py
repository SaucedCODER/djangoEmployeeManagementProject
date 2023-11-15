from django.urls import path
from . import views

app_name = 'employees'
urlpatterns = [
    path('open_attendance/', views.openAttendance, name='open_attendance'),
    path('set_attendance/<str:date>/', views.setAttendance, name='set_attendance')



  
]