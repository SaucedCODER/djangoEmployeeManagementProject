from django.urls import path
from . import views
app_name = 'projects'
urlpatterns = [
    path('', views.projects, name='projects'),
    path('update/<int:pk>', views.updateProject, name='update'),
    path('project/<int:pk>', views.viewProject, name='view'),
    path('task/<int:pk>', views.updateTask, name='update'),

    # path('newTask/', views.newTask, name='newTask'),
    # path('updateTask/', views.updateTask, name='updateTask'),
    # path('deleteTask/', views.deleteTask, name='deleteTask'),

]