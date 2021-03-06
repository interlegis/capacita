from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views

urlpatterns = [
    url(r'^orgao/$', views.orgao, name='orgao'),
    url(r'^orgao/(?P<pk>\d+)/edit/$', views.orgao_edit, name='orgao_edit'),
    url(r'^orgao/(?P<id>\d+)/delete$', views.orgao_delete, name='orgao_delete'),
    url(r'^orgao/(?P<id>\d+)/invisible$', views.orgao_invisible, name='orgao_invisible'),
    url(r'^orgao/(?P<id>\d+)/visible$', views.orgao_visible, name='orgao_visible'),
    url(r'^orgao/new/$', views.orgao_new, name='orgao_new'),
    url(r'^orgao/(?P<pk>\d+)/gestores_orgao/$', views.gestores_orgao, name='gestores_orgao'),
]
