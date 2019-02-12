from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^login/$', LoginView.as_view(), name='login'),
    #url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^login/$', django_cas_ng.views.login, name='cas_ng_login'),
    url(r'^logout/$', django_cas_ng.views.logout, {'next_page': '/login/'} ,name='cas_ng_logout'),
    url(r'^callback/$', django_cas_ng.views.callback, name='cas_ng_proxy_callback'),
    url(r'^relatorio/$', views.relatorio, name='relatorio'),
   # url(r'^avaliacao_cursos/$', views.avaliacao_cursos, name='avaliacao_cursos'),
    url(r'^error/$', views.error, name='error'),
    url(r'^orgao/(?P<pk>\d+)/mudanca/$', views.mudanca_orgao, name='mudanca_orgao'),
]
