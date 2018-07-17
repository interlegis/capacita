from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'} ,name='logout'),
    url(r'^necessidade/$', views.necessidade, name='necessidade'),
    url(r'^necessidade/(?P<pk>\d+)/edit/$', views.necessidade_edit, name='necessidade_edit'),
    url(r'^necessidade/(?P<pk>\d+)/show/$', views.necessidade_show, name='necessidade_show'),
    url(r'^necessidade/(?P<pk>\d+)/$', views.necessidade_delete, name='necessidade_delete'),
    url(r'^necessidade/new/$', views.necessidade_new, name='necessidade_new'),
    url(r'^plano/$', views.plano, name="plano"),
    url(r'^plano/new/$', views.plano_new, name="plano_new"),
    url(r'^plano/(?P<id>\d+)/edit/$', views.plano_edit, name='plano_edit'),
    url(r'^plano/(?P<id>\d+)/$', views.plano_delete, name='plano_delete'),
    url(r'^plano/(?P<id>\d+)/show/$', views.plano_show, name='plano_show'),
    url(r'^orgao/$', views.orgao, name='orgao'),
    url(r'^orgao/(?P<pk>\d+)/edit/$', views.orgao_edit, name='orgao_edit'),
    url(r'^orgao/(?P<id>\d+)/$', views.orgao_delete, name='orgao_delete'),
    url(r'^orgao/new/$', views.orgao_new, name='orgao_new'),
]