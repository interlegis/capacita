from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views

urlpatterns = [
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^usuarios/new/$', views.usuario_new, name='usuario_new'),
    url(r'^usuarios/(?P<pk>\d+)/edit/$', views.usuario_edit, name='usuario_edit'),
    url(r'^usuarios/(?P<pk>\d+)/orgao/$', views.usuario_orgao_adicionar, name='usuario_orgao_adicionar'),
    url(r'^usuarios/(?P<pk>\d+)/(?P<orgao>\d+)/orgao/$', views.usuario_orgao_deletar, name='usuario_orgao_deletar'),
]
