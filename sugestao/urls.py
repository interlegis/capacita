from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views

urlpatterns = [
    url(r'^sugestao/$', views.sugestao, name='sugestao'),
    url(r'^sugestao/new/$', views.sugestao_new, name='sugestao_new'),
]
