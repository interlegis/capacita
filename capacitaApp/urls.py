from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import django_cas_ng.views
from capacita.settings import DEBUG


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^relatorio/$', views.relatorio, name='relatorio'),
    url(r'^error/$', views.error, name='error'),
    url(r'^processo_capacitacao/$', views.processo_capacitacao, name='processo_capacitacao'),
    url(r'^perguntas_frequentes/$', views.perguntas_frequentes, name='perguntas_frequentes'),
    url(r'^manual/$', views.manual, name='manual'),
    url(r'^orgao/(?P<pk>\d+)/mudanca/$', views.mudanca_orgao, name='mudanca_orgao'),
    url(r'^notificacao/$', views.notificacao, name='notificacao'),
    url(r'^api_get_notificacoes/$', views.api_get_notificacoes, name='api_get_notificacoes'),
    url(r'^api_set_notificacao/$', views.api_set_notificacao, name='api_set_notificacao'),

]


if DEBUG:
    urlpatterns = [
        url(r'^login/$', LoginView.as_view(), name='login'),
        url(r'^logout/$', LogoutView.as_view(), name='logout')] + urlpatterns
else:
    urlpatterns = [
        url(r'^login/$', django_cas_ng.views.login, name='cas_ng_login'),
        url(r'^logout/$', django_cas_ng.views.logout, {'next_page': '/login/'} ,name='cas_ng_logout'),
        url(r'^callback/$', django_cas_ng.views.callback, name='cas_ng_proxy_callback')] + urlpatterns
