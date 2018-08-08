from .models import *
import django_filters

class PlanoFilter(django_filters.FilterSet):
    class Meta:
        model = Plano_Capacitacao
        fields = ['cod_orgao', ]

class AreaFilter(django_filters.FilterSet):
    class Meta:
        model = Sub_Area_Conhecimento
        fields = ['cod_area_conhecimento', ]