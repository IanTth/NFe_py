from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'xml_gender', views.gender),
    url(r'', views.home ),

] + static(settings.STATIC_URL)
