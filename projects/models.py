from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


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

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)