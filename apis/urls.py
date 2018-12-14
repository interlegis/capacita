from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views

urlpatterns = [
    url(r'^api/areas/$', views.api_areas, name='api_areas'),
    url(r'^api/planos/$', views.api_planos, name='api_planos'),
    url(r'^api/tipos_treinamento/$', views.api_tipos_treinamento, name='api_tipos'),
    url(r'^api/treinamentos/$', views.api_cursos, name='api_cursos'),
]
