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
<<<<<<< HEAD
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
   #  url(r'^login/$', django_cas_ng.views.login, name='cas_ng_login'),
   # url(r'^logout/$', django_cas_ng.views.logout, {'next_page': '/login/'} ,name='cas_ng_logout'),
   # url(r'^callback/$', django_cas_ng.views.callback, name='cas_ng_proxy_callback'),
=======
>>>>>>> ac7479a640c5d552725ccb93a27c8d9544a145d6
    url(r'^relatorio/$', views.relatorio, name='relatorio'),
    url(r'^error/$', views.error, name='error'),
    url(r'^processo_capacitacao/$', views.processo_capacitacao, name='processo_capacitacao'),
    url(r'^perguntas_frequentes/$', views.perguntas_frequentes, name='perguntas_frequentes'),
    url(r'^manual/$', views.manual, name='manual'),
    url(r'^orgao/(?P<pk>\d+)/mudanca/$', views.mudanca_orgao, name='mudanca_orgao'),
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
