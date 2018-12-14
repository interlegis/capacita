from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^tipos_treinamento/$', views.tipos_treinamento, name='tipos_treinamento'),
    url(r'^tipo_treinamento/(?P<id>\d+)/edit/$', views.tipo_treinamento_edit, name='tipo_treinamento_edit'),
    url(r'^tipo_treinamento/new/$', views.tipo_treinamento_new, name='tipo_treinamento_new'),
    url(r'^tipo_treinamento/(?P<pk>\d+)/delete$', views.tipo_treinamento_delete, name='tipo_treinamento_delete'),
    url(r'^tipo_treinamento/(?P<pk>\d+)/undelete$', views.tipo_treinamento_undelete, name='tipo_treinamento_undelete'),
]
