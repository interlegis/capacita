from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
import django_cas_ng.views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^$', auth_views.login, name='login'),
    # url(r'^$', auth_views.logout, name='logout'),
    url(r'^login/$', django_cas_ng.views.login, name='cas_ng_login'),
    url(r'^logout/$', django_cas_ng.views.logout, {'next_page': '/login/'} ,name='cas_ng_logout'),
    url(r'^callback/$', django_cas_ng.views.callback, name='cas_ng_proxy_callback'),
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
    url(r'^tipo/$', views.tipo, name='tipo'),
    url(r'^tipo/(?P<id>\d+)/edit/$', views.tipo_edit, name='tipo_edit'),
    url(r'^tipo/new/$', views.tipo_new, name='tipo_new'),
    url(r'^areas/$', views.areas, name='areas'),
    url(r'^api/areas/$', views.api_areas, name='api_areas'),
    url(r'^api/subareas/$', views.api_subareas, name='api_subareas'),
    url(r'^subareas/new/$', views.subareas_new, name='subareas_new'),
    url(r'^subareas/(?P<id>\d+)/$', views.subarea_delete, name='subarea_delete'),
    url(r'^subarea/(?P<pk>\d+)/edit/$', views.sub_area_edit, name='sub_area_edit'),
    url(r'^relatorio/$', views.relatorio, name='relatorio')
]