from django import forms
from django.contrib import admin
from .models import Project, Task, User

class TaskAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
         # Customize the 'assign' field queryset based on the associated project
        if 'project' in self.fields:
            project_id = self.cleaned_data.get('project')
            try:
                project_id = int(project_id)
                project = Project.objects.get(pk=project_id)
                self.fields['assign'].queryset = project.assign.all()
            except (ValueError, Project.DoesNotExist):
                # Handle the case where project_id is not a valid integer or project doesn't exist
                self.fields['assign'].queryset = User.objects.none()

class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm  # Use the custom form
    list_display = ['task_name', 'project']
    list_filter = ['project']
    search_fields = ['project']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']
    search_fields = ['name', 'status']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
