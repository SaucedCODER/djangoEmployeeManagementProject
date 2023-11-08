from django.contrib import admin
from .models import Project
from .models import Task
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']
    search_fields = ['name', 'status']
    class Meta:
        model = Project

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name','project']
    list_filter = ['project', ]
    search_fields = ['project']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)