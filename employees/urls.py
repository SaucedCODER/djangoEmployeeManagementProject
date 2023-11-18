from django.urls import path
from . import views

app_name = 'employees'
urlpatterns = [
    path('open_attendance/', views.openAttendance, name='open_attendance'),
    path('set_attendance/<str:date>/', views.setAttendance, name='set_attendance'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.create_appointment, name='create_appointment'),
    path('appointments/update/<int:pk>', views.update_appointment, name='update_appointment'),
    path('appointments/delete/<int:pk>', views.delete_appointment, name='delete_appointment'),
    path('appointments/view/<int:pk>', views.view_appointment, name='view_appointment'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/view/', views.view_profile, name='view_profile'),
    path('change_password/', views.change_password, name='change_password'),
]# 

