from django.urls import path
from . import views
app_name = 'projects'
urlpatterns = [
    path('', views.projects, name='projects'),
    path('new/', views.newProject, name='new'),
    path('update/<int:pk>', views.updateProject, name='update'),
    path('project/<int:pk>', views.viewProject, name='view'),
    path('delete/<int:pk>', views.deleteProject, name='delete'),
    # path('newTask/', views.newTask, name='newTask'),
    # path('updateTask/', views.updateTask, name='updateTask'),
    # path('deleteTask/', views.deleteTask, name='deleteTask'),

]