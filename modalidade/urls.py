from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views

urlpatterns = [
    url(r'^modalidade/$', views.modalidade, name='modalidade'),
    url(r'^modalidade/(?P<pk>\d+)/delete$', views.modalidade_delete, name='modalidade_delete'),
    url(r'^modalidade/(?P<pk>\d+)/invisible$', views.modalidade_invisible, name='modalidade_invisible'),
    url(r'^modalidade/(?P<pk>\d+)/visible$', views.modalidade_visible, name='modalidade_visible'),
    url(r'^modalidade/(?P<pk>\d+)/edit/$', views.modalidade_edit, name='modalidade_edit'),
    url(r'^modalidade/new/$', views.modalidade_new, name='modalidade_new'),
]
