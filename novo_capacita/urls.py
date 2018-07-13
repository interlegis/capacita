from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^necessidade/(?P<pk>\d+)/edit/$', views.necessidade_edit, name='necessidade_edit'),
    url(r'^necessidade/new/$', views.necessidade_new, name='necessidade_new'),
    url(r'^plano/$', views.plano, name="plano"),
    url(r'^plano/new/$', views.plano_new, name="plano_new")
]