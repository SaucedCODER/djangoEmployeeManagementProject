from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.decorators import user_passes_test
def is_staff(user):
    return user.is_staff

app_name = 'core'
urlpatterns = [
    path("",views.home, name="home"),
    path("login/",views.login_user, name="login"),
    path("logout/",views.logout_user, name="logout"),
    path('admin/', user_passes_test(is_staff)(RedirectView.as_view(url='/admin/')),name='admin'),
    path('mark-as-read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
