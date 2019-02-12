from django.contrib import admin
from capacitaApp.models import *
from plano.models import *
from necessidade.models import *

admin.site.register(Area_Conhecimento)
admin.site.register(Necessidade)
admin.site.register(Nivel)
admin.site.register(Orgao)
admin.site.register(Plano_Capacitacao)
admin.site.register(Prioridade)
admin.site.register(Profile)
admin.site.register(Treinamento)
admin.site.register(Objetivo_Treinamento)
admin.site.register(Modalidade_Treinamento)
admin.site.register(Necessidade_Orgao)
