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


from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileUpdateForm(forms.ModelForm):
    profession = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    avatar = forms.ImageField(required=False)
    class Meta:
        model = UserProfile
        fields = ['avatar','profession']

    def clean_avatar(self):
        cleaned_avatar = self.cleaned_data.get('avatar')

        if cleaned_avatar:
            try:

                # validate content type
                main, sub = cleaned_avatar.content_type.split('/')
                if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                    raise forms.ValidationError(u'Please use a JPEG, '
                        'GIF, or PNG image.')
              

            except AttributeError:
                """
                Handles the case when we are updating the user profile
                and do not supply a new avatar
                """
                pass

        return cleaned_avatar
    
from django.urls import reverse
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
        self.fields['password'].required = False
        
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


from django.contrib.auth.forms import PasswordChangeForm
class CustomPasswordChangeForm(PasswordChangeForm):
    new_password_again = forms.CharField(
        label="New Password (again)",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password_again'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password1')
        new_password_again = cleaned_data.get('new_password_again')

        # Check if the two new password fields match
        if new_password and new_password_again and new_password != new_password_again:
            raise forms.ValidationError("The two new password fields didn't match.")

        return cleaned_data
