from django.contrib import admin, messages
from .models import Attendance
from django.contrib.auth.models import User
from django import forms
from .models import Appointment
from core.utils import create_notification
# my_app/admin.py
from .models import UserProfile

admin.site.register(UserProfile)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_time', 'status', 'description', 'notes')
    list_filter = ('user', 'date_time', 'status')
    search_fields = ('user__username', 'description', 'notes')
    actions = ['approve_selected', 'reject_selected']

    def approve_selected(self, request, queryset):
        queryset.update(status='approved')
        for appointment in queryset:
            formatted_date_time = appointment.date_time.strftime("%B %d, %Y, %I:%M:%S %p")
            create_notification(appointment.user, f"Your appointment on {formatted_date_time} has been approved.")

    approve_selected.short_description = "Mark selected appointments as Approved"

    def reject_selected(self, request, queryset):
        queryset.update(status='rejected')
        for appointment in queryset:
            formatted_date_time = appointment.date_time.strftime("%B %d, %Y, %I:%M:%S %p")
            create_notification(appointment.user, f"Your appointment on {formatted_date_time} has been rejected.")

    reject_selected.short_description = "Mark selected appointments as Rejected"

admin.site.register(Appointment, AppointmentAdmin)
from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from .models import Attendance
from django.forms.widgets import CheckboxInput
User = get_user_model()

class NoteCheckboxInput(CheckboxInput):
    def render(self, name, value, attrs=None, renderer=None):
        note_html = '<p style="margin-top: 5px; color: #888; font-style: italic;">Note: Initial creation is always open, system rules.</p>'
        return super().render(name, value, attrs=attrs) + note_html

class AttendanceAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Check if 'is_open' exists in the form
        if 'is_open' in self.fields:
            self.fields['is_open'].widget = NoteCheckboxInput()
    def clean_user(self):
        # Make sure the user field is not changed during editing
        if self.instance and self.cleaned_data['user'] != self.instance.user:
            raise forms.ValidationError("You cannot change the user for an existing record.")

        # Check for duplicate records with the same user and date
        user = self.cleaned_data['user']
        date = self.cleaned_data['date']

        existing_records = Attendance.objects.filter(user=user, date=date).exclude(pk=self.instance.pk if self.instance else None)

        if existing_records.exists():
            raise forms.ValidationError('An attendance record for this user and date already exists.')

        return user
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendanceAdmin(admin.ModelAdmin):
    form = AttendanceAdminForm
    list_display = ('date', 'user', 'status', 'is_open')
    list_filter = ('status', 'is_open')
    search_fields = ('date', 'user__username')  # Adjust for searching by user's username
    date_hierarchy = 'date'  # Add date hierarchy for easy navigation
 
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Check if 'status' and 'is_open' fields should be disabled based on user role
        if obj and obj.user.is_staff:
            # If the selected user is an admin or staff, disable 'status' and remove 'is_open'
            form.base_fields['status'].disabled = True

        elif obj:
            # If the selected user is not an admin or staff, enable 'status' and remove 'is_open'
            form.base_fields['status'].disabled = False
            form.base_fields.pop('is_open', None)

        

        return form

    def save_model(self, request, obj, form, change):
        # Set 'is_open' to True for the initial creation
        if not change:
            obj.is_open = True
            messages.info(request, "Attendance record created. 'is_open' has been automatically set to 'True' for the initial creation.")

        # Save the model instance
        obj.save()

        # Check if 'is_open' is set to False
        if not obj.is_open:
            # Get all users
            messages.info(request, "Attendance record updated. 'is_open' set to 'False'. 'Not Set' attendance records have been created for users who haven't marked their attendance.")

            users = User.objects.all()

            # Create 'not_set' attendance records for all users for the specified date
            for user in users:
                # Check if the 'not_set' attendance record already exists for the user and date
                if not Attendance.objects.filter(user=user, date=obj.date).exists():
                    # Create 'not_set' attendance record
                    Attendance.objects.create(user=user, date=obj.date, status='not_set')

admin.site.register(Attendance, AttendanceAdmin)




from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        exclude = ('user_permissions', 'groups',)

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        # Add or customize other fields as needed
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

# Register the custom UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

