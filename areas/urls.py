from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^areas/$', views.areas, name='areas'),
    url(r'^area/new/$', views.area_new, name='area_new'),
    url(r'^area/(?P<id>\d+)/edit/$', views.area_edit, name='area_edit'),
    url(r'^area/(?P<pk>\d+)/delete$', views.area_delete, name='area_delete'),
    url(r'^area/(?P<pk>\d+)/undelete$', views.area_undelete, name='area_undelete'),
    url(r'^area/new/$', views.area_new, name='area_new'),
]
