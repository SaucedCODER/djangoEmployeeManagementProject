from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
# remove group table
admin.site.unregister(Group)

admin.site.site_title = "CTinnovation"
admin.site.site_header = "CivileTech Innovation"
admin.site.index_title = "Admin Panel"
