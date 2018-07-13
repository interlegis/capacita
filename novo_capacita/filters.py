from .models import *
import django_filters

class PlanoFilter(django_filters.FilterSet):
    class Meta:
        model = Plano_Capacitacao
        fields = ['cod_orgao', ]