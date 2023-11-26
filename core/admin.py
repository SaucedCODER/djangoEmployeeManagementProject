from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.site_title = "CTinnovation"
admin.site.site_header = "CivilTech Innovation"
admin.site.index_title = "Admin Panel"

