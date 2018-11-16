from .models import *
import django_filters

class NecessidadeFilter(django_filters.FilterSet):
    class Meta:
        model = Necessidade
        fields = ['qtd_servidor', ]
