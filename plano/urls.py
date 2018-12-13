from django.conf.urls import url
from django.urls import path, include
from plano import views


urlpatterns = [
    url(r'^plano/$', views.plano, name="plano"),
    url(r'^plano/new/$', views.plano_new, name="plano_new"),
    url(r'^plano/(?P<id>\d+)/edit/$', views.plano_edit, name='plano_edit'),
    url(r'^plano/(?P<id>\d+)/delete$', views.plano_delete, name='plano_delete'),
    url(r'^plano/(?P<id>\d+)/undelete$', views.plano_undelete, name='plano_undelete'),
    url(r'^plano/(?P<id>\d+)/show/$', views.plano_show, name='plano_show'),
]
