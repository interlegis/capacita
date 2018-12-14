from django.conf.urls import url
from django.urls import path, include
from necessidade import views


urlpatterns = [
    url(r'^necessidade/$', views.necessidade, name='necessidade'),
    url(r'^necessidade/(?P<pk>\d+)/edit/$', views.necessidade_edit, name='necessidade_edit'),
    url(r'^necessidade/(?P<pk>\d+)/show/$', views.necessidade_show, name='necessidade_show'),
    url(r'^necessidade/(?P<pk>\d+)/delete$', views.necessidade_delete, name='necessidade_delete'),
    url(r'^necessidade/(?P<pk>\d+)/approve$', views.necessidade_approve, name='necessidade_approve'),
    url(r'^necessidade/(?P<pk>\d+)/disapprove$', views.necessidade_disapprove, name='necessidade_disapprove'),
    url(r'^necessidade/(?P<pk>\d+)/close$', views.necessidade_orgao_close, name='necessidade_orgao_close'),
    url(r'^necessidade/(?P<pk>\d+)/(?P<pk_atual>\d+)/importar$', views.importar_necessidade, name='importar_necessidade'),
    url(r'^necessidade/new/$', views.necessidade_new, name='necessidade_new'),
]
