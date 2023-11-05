from django.urls import path
from . import views
app_name = 'projects'
urlpatterns = [
    path('', views.projects, name='projects'),
    path('newProject/', views.newProject, name='newProject'),
    path('newTask/', views.newTask, name='newTask'),
]