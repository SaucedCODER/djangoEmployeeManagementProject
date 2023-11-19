from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('not_set', 'Not Set'),
        ('present', 'Present'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES, default='not_set')
    is_open = models.BooleanField(default=False)

    @classmethod
    def present_days_count(cls, user):
        return cls.objects.filter(user=user, status='present').count() or 0
    
    @classmethod
    def mark_attendance(cls, user, date):
        attendance, created = cls.objects.get_or_create(
            user=user,
            date=date,
            defaults={'status': 'present'}
        )
        # If the record already exists, update the status to 'present'
        if not created:
            attendance.status = 'present'
            attendance.save()
            return False
        else:
            return True

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.get_status_display()}"
# class CustomUserManager(BaseUserManager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_staff=False, is_superuser=False)

# Appointment model

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    title = models.CharField(max_length=80, default=None, null=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date_time}"

#custon userProfile model


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/') 
    profession = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.user.username
    
    

