# calculator/urls.py
from django.urls import path
from .views import calculate_load

app_name = 'calculator'
urlpatterns = [
    path('calculate/', calculate_load, name='calculate_load'),
]
