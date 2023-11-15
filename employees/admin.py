# your_app/admin.py
from django.contrib import admin
from .models import Attendance
from django.contrib.auth.models import User

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'status')
    list_filter = ('status',)
    search_fields = ('date', 'user__username')  # Adjust for searching by user's username
    date_hierarchy = 'date'  # Add date hierarchy for easy navigation


