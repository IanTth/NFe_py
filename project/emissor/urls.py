from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'registrar', views.register),
    url(r'pagina_inicial', views.home),
    url(r'', views.login ),

] + static(settings.STATIC_URL)
