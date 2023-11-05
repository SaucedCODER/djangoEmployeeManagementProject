from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'core'
urlpatterns = [
    path("",views.home, name="home"),
    path("login/",views.login_user, name="login"),
    path("logout/",views.logout_user, name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
