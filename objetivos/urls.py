from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views

urlpatterns = [
    url(r'^objetivos/$', views.objetivos, name='objetivos'),
    url(r'^objetivo/(?P<pk>\d+)/delete$', views.objetivo_delete, name='objetivo_delete'),
    url(r'^objetivo/(?P<pk>\d+)/undelete$', views.objetivo_undelete, name='objetivo_undelete'),
    url(r'^objetivo/(?P<pk>\d+)/edit/$', views.objetivo_edit, name='objetivo_edit'),
    url(r'^objetivo/new/$', views.objetivo_new, name='objetivo_new'),
]
