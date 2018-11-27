from django.conf.urls import url
from capacitaApp import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views

urlpatterns = [
    url(r'^$', views.home, name='home'),
#    url(r'^login/$', LoginView.as_view(), name='login'),
#    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^login/$', django_cas_ng.views.login, name='cas_ng_login'),
    url(r'^logout/$', django_cas_ng.views.logout, {'next_page': '/login/'} ,name='cas_ng_logout'),
    url(r'^callback/$', django_cas_ng.views.callback, name='cas_ng_proxy_callback'),
    url(r'^necessidade/$', views.necessidade, name='necessidade'),
    url(r'^necessidade/(?P<pk>\d+)/edit/$', views.necessidade_edit, name='necessidade_edit'),
    url(r'^necessidade/(?P<pk>\d+)/show/$', views.necessidade_show, name='necessidade_show'),
    url(r'^necessidade/(?P<pk>\d+)/delete$', views.necessidade_delete, name='necessidade_delete'),
    url(r'^necessidade/new/$', views.necessidade_new, name='necessidade_new'),
    url(r'^plano/$', views.plano, name="plano"),
    url(r'^plano/new/$', views.plano_new, name="plano_new"),
    url(r'^plano/(?P<pk>\d+)/edit/$', views.plano_edit, name='plano_edit'),
    url(r'^plano/(?P<pk>\d+)/delete$', views.plano_delete, name='plano_delete'),
    url(r'^plano/(?P<id>\d+)/show/$', views.plano_show, name='plano_show'),
    url(r'^treinamentos/$', views.treinamentos, name='treinamentos'),
    url(r'^treinamento/(?P<pk>\d+)/delete$', views.treinamento_delete, name='treinamento_delete'),
    url(r'^treinamento/(?P<pk>\d+)/edit/$', views.treinamento_edit, name='treinamento_edit'),
    url(r'^treinamento/new/$', views.treinamento_new, name='treinamento_new'),
    url(r'^orgao/$', views.orgao, name='orgao'),
    url(r'^orgao/(?P<pk>\d+)/edit/$', views.orgao_edit, name='orgao_edit'),
    url(r'^orgao/(?P<id>\d+)/delete$', views.orgao_delete, name='orgao_delete'),
    url(r'^orgao/new/$', views.orgao_new, name='orgao_new'),
    url(r'^tipos_treinamento/$', views.tipos_treinamento, name='tipos_treinamento'),
    url(r'^tipo_treinamento/(?P<id>\d+)/edit/$', views.tipo_treinamento_edit, name='tipo_treinamento_edit'),
    url(r'^tipo_treinamento/new/$', views.tipo_treinamento_new, name='tipo_treinamento_new'),
    url(r'^tipo_treinamento/(?P<pk>\d+)/delete$', views.tipo_treinamento_delete, name='tipo_treinamento_delete'),
    url(r'^area/new/$', views.area_new, name='area_new'),
    url(r'^api/areas/$', views.api_areas, name='api_areas'),
    url(r'^api/planos/$', views.api_planos, name='api_planos'),
    url(r'^api/tipos_treinamento/$', views.api_tipos_treinamento, name='api_tipos'),
    url(r'^api/treinamentos/$', views.api_cursos, name='api_cursos'),
    url(r'^areas/$', views.areas, name='areas'),
    url(r'^area/(?P<id>\d+)/edit/$', views.area_edit, name='area_edit'),
    url(r'^area/(?P<pk>\d+)/delete$', views.area_delete, name='area_delete'),
    url(r'^area/new/$', views.area_new, name='area_new'),
    url(r'^relatorio/$', views.relatorio, name='relatorio'),
    url(r'^modalidade/$', views.modalidade, name='modalidade'),
    url(r'^modalidade/(?P<pk>\d+)/delete$', views.modalidade_delete, name='modalidade_delete'),
    url(r'^modalidade/(?P<pk>\d+)/edit/$', views.modalidade_edit, name='modalidade_edit'),
    url(r'^modalidade/new/$', views.modalidade_new, name='modalidade_new'),
    url(r'^eventos/$', views.eventos, name='eventos'),
    url(r'^evento/(?P<pk>\d+)/delete$', views.evento_delete, name='evento_delete'),
    url(r'^evento/(?P<pk>\d+)/edit/$', views.evento_edit, name='evento_edit'),
    url(r'^evento/new/$', views.evento_new, name='evento_new'),
    url(r'^objetivos/$', views.objetivos, name='objetivos'),
    url(r'^objetivo/(?P<pk>\d+)/delete$', views.objetivo_delete, name='objetivo_delete'),
    url(r'^objetivo/(?P<pk>\d+)/edit/$', views.objetivo_edit, name='objetivo_edit'),
    url(r'^objetivo/new/$', views.objetivo_new, name='objetivo_new'),
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^usuarios/permissao/$', views.usuarios_permissao, name='usuarios_permissao'),
    url(r'^usuarios/new/$', views.usuario_new, name='usuario_new'),
    url(r'^usuarios/(?P<pk>\d+)/edit/$', views.usuario_edit, name='usuario_edit'),
#    url(r'^avaliacao_cursos/$', views.avaliacao_cursos, name='avaliacao_cursos'),
    url(r'^error/$', views.error, name='error')
]
