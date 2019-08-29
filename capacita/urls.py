from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
   path('', include('plano.urls')),
   path('', include('necessidade.urls')),
   path('', include('capacitaApp.urls')),
   path('', include('treinamento.urls')),
   path('', include('objetivos.urls')),
   path('', include('orgao.urls')),
   path('', include('tipo_treinamento.urls')),
   path('', include('areas.urls')),
   path('', include('usuario.urls')),
   path('', include('modalidade.urls')),
   path('', include('apis.urls')),
   path('', include('sugestao.urls')),
]
