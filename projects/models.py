from django.db import models
from django.contrib.auth.models import User, BaseUserManager

from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date


status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)
taskStatus = (
    ('1', 'Not Started'),
    ('2', 'In Progress'),
    ('3', 'Completed'),
)
due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=80)
    assign = models.ManyToManyField(User)
    status = models.CharField(max_length=7, choices=status, default=1)
    dead_line = models.DateField()
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(blank=True)

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assign = models.ManyToManyField(User)
    task_name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=taskStatus, default=1)
    start = models.DateField()
    end = models.DateField()
    challenges = models.CharField(max_length=80, default=None, null=True, blank=True)
    progress_update = models.CharField(max_length=80, default=None, null=True, blank=True)

    def remaining_days(self):
        from datetime import date

        today = date.today()
        remaining_days = (self.end - today).days
        return remaining_days
    
    @classmethod
    def overdue_tasks(cls):
        today = date.today()
        return cls.objects.filter(end__lt=today, status__in=['1', '2']).count() or 0 

    @classmethod
    def completed_tasks(cls):
        return cls.objects.filter(status='3').count() or 0 
    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)
