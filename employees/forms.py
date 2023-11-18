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


from django.core.files.images import get_image_dimensions
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')

        if avatar:
            try:
                w, h = get_image_dimensions(avatar)

                # validate dimensions
                max_width = max_height = 100
                if w > max_width or h > max_height:
                    raise forms.ValidationError(
                        u'Please use an image that is '
                         '%s x %s pixels or smaller.' % (max_width, max_height))

                # validate content type
                main, sub = avatar.content_type.split('/')
                if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                    raise forms.ValidationError(u'Please use a JPEG, '
                        'GIF, or PNG image.')

                # validate file size
                if len(avatar) > (20 * 1024):
                    raise forms.ValidationError(
                        u'Avatar file size may not exceed 20k.')

            except AttributeError:
                """
                Handles case when we are updating the user profile
                and do not supply a new avatar
                """
                pass

        return avatar
