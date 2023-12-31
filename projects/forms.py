from django import forms
from django.utils.text import slugify
from .models import Task
from .models import Project
from django.contrib.auth.models import User

statuses = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)


class TaskCreationForm(forms.ModelForm):
    task_name = forms.CharField(max_length=80)
    start = forms.DateField()
    end = forms.DateField()
    challenges = forms.CharField(max_length=80)
    progress_update = forms.CharField(max_length=80)

    class Meta:
        model = Task
        fields = ['task_name', 'status', 'start', 'end', 'challenges','progress_update']
        exclude = ('assign',)


    def save(self, commit=True):
        task = super(TaskCreationForm, self).save(commit=False)
        task.task_name = self.cleaned_data['task_name']
        task.status = self.cleaned_data['status']
        task.start = self.cleaned_data['start']
        task.end = self.cleaned_data['end']
        task.challenges = self.cleaned_data['challenges']
        task.progress_update = self.cleaned_data['progress_update']
        task.save()
   
        if commit:
            task.save()

        return task


    def __init__(self, *args, **kwargs):
        super(TaskCreationForm, self).__init__(*args, **kwargs)
   
        self.fields['task_name'] = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control','readonly': True})
        )
        self.fields['status'] = forms.ChoiceField(
            choices=statuses,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Status'
            
        })
        )
        self.fields['start'] = forms.DateField(
            widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date','placeholder':'Start, type a date','readonly': True})
        )
        self.fields['end'] = forms.DateField(
            widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date','placeholder':'End, type a date','readonly': True
            })
        )
        self.fields['challenges'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Type here the challenges...'
        })
        self.fields['progress_update'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Type here the progress_update...'
        })



class ProjectCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    dead_line = forms.DateField()
    complete_per = forms.FloatField(min_value=0, max_value=100)
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Project description...', 'readonly': True}))
 
    class Meta:
        model = Project
        fields = ['name', 'status', 'dead_line', 'complete_per', 'description']
        exclude = ('assign',)


    def save(self, commit=True):
        Project = super(ProjectCreationForm, self).save(commit=False)
        Project.name = self.cleaned_data['name']
        Project.status = self.cleaned_data['status']
        Project.dead_line = self.cleaned_data['dead_line']
        Project.complete_per = self.cleaned_data['complete_per']
        Project.description = self.cleaned_data['description']
        Project.save()

        if commit:
            Project.save()

        return Project


    def __init__(self, *args, **kwargs):
        super(ProjectCreationForm, self).__init__(*args, **kwargs)
       
        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Project Name'
             ,'readonly': True
        })

        self.fields['status'] = forms.ChoiceField(
            choices=statuses,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Status'
        })
        )

        self.fields['dead_line'].widget = forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Deadline, type a date'
             ,'readonly': True
        })

        self.fields['complete_per'].widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Complete %',
            'min': 0,
            'max': 100,
            'readonly': True
        })
     