from .models import *
import django_filters

class PlanoFilter(django_filters.FilterSet):
    class Meta:
        model = Plano_Capacitacao
        fields = ['cod_orgao', ]

class SubAreaFilter(django_filters.FilterSet):
    class Meta:
        model = Sub_Area_Conhecimento
        fields = ['cod_area_conhecimento_id', ]

class NecessidadeFilter(django_filters.FilterSet):
    class Meta: 
        model = Necessidade
        fields = ['qtd_servidor', ]