# Forms settings for appointment settings
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    title = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    date_time = forms.DateTimeField(
        widget=forms.DateInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'form-control','type': 'datetime-local'})
    )
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
   
    class Meta:
        model = Appointment
        fields = ['title','date_time', 'description']
class AppointmentFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'All'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
