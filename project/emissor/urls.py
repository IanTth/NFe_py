from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'registrar', views.register),
    url(r'home', views.home),
    url(r'', views.login ),

] + static(settings.STATIC_URL)
