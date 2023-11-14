from django.urls import path
from . import views
app_name = 'projects'
urlpatterns = [
    path('', views.projects, name='projects'),
    path('update/<int:pk>', views.updateProject, name='update'),
    path('details/<int:pk>', views.viewProject, name='view'),
    path('updatetask/<int:pk>', views.updateTask, name='updateTask'),
    path('viewtask/<int:pk>', views.viewTask, name='viewTask'),


    # path('newTask/', views.newTask, name='newTask'),
    # path('updateTask/', views.updateTask, name='updateTask'),
    # path('deleteTask/', views.deleteTask, name='deleteTask'),

]