from django import forms
from django.contrib import admin
from .models import Project, Task, User

class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the 'assign' field queryset based on the associated project
        if 'project' in self.fields:
            project_id = self['project'].value()
            if project_id is not None:
                try:
                    project_id = int(project_id)
                    project = Project.objects.get(pk=project_id)
                    self.fields['assign'].queryset = project.assign.all()
                except (ValueError, Project.DoesNotExist):
                    # Handle the case where project_id is not a valid integer or project doesn't exist
                    self.fields['assign'].queryset = User.objects.none()
            else:
                # If no project is selected, set an empty queryset for 'assign'
                self.fields['assign'].queryset = User.objects.none()

class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    list_display = ['task_name', 'project']
    list_filter = ['project']
    search_fields = ['project']
    def get_form(self, request, obj=None, **kwargs):
        # Create a dynamic form with the current request
        form = super().get_form(request, obj, **kwargs)
        first_project = Project.objects.filter(assign__isnull=False).first()
        if first_project:
            form.base_fields['project'].initial = first_project

        return form

    def save_model(self, request, obj, form, change):
        # Override save_model to set the current user as the task creator
        if not obj.pk:
            obj.creator = request.user
        super().save_model(request, obj, form, change)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']
    search_fields = ['name', 'status']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
