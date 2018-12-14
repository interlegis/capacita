from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views

urlpatterns = [
    url(r'^treinamentos/$', views.treinamentos, name='treinamentos'),
    url(r'^treinamento/(?P<pk>\d+)/delete$', views.treinamento_delete, name='treinamento_delete'),
    url(r'^treinamento/(?P<pk>\d+)/undelete$', views.treinamento_undelete, name='treinamento_undelete'),
    url(r'^treinamento/(?P<pk>\d+)/edit/$', views.treinamento_edit, name='treinamento_edit'),
    url(r'^treinamento/new/$', views.treinamento_new, name='treinamento_new'),
]
