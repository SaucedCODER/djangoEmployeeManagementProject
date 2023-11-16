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


# employees/admin.py
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_time', 'status', 'description', 'notes')
    list_filter = ('user', 'date_time', 'status')
    search_fields = ('user__username', 'description', 'notes')
    actions = ['approve_selected', 'reject_selected']

    def approve_selected(self, request, queryset):
        queryset.update(status='approved')

    def reject_selected(self, request, queryset):
        queryset.update(status='rejected')

admin.site.register(Appointment, AppointmentAdmin)

