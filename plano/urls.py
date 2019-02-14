from django.conf.urls import url
from django.urls import path, include
from plano import views


urlpatterns = [
    url(r'^plano/$', views.plano, name="plano"),
    url(r'^plano/new/$', views.plano_new, name="plano_new"),
    url(r'^plano/(?P<id>\d+)/edit/$', views.plano_edit, name='plano_edit'),
    url(r'^plano/(?P<id>\d+)/delete$', views.plano_delete, name='plano_delete'),
    url(r'^plano/(?P<id>\d+)/invisible$', views.plano_invisible, name='plano_invisible'),
    url(r'^plano/(?P<id>\d+)/visible$', views.plano_visible, name='plano_visible'),
    url(r'^plano/(?P<id>\d+)/show/$', views.plano_show, name='plano_show'),
]
