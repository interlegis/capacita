# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group
from capacitaApp.models import *

class TreinamentoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        emptyField = [('', '---------')]
        super(TreinamentoForm, self).__init__(*args, **kwargs)
        # areas_conhecimento
        self.fields['cod_area_conhecimento'].queryset = Area_Conhecimento.objects.all().exclude(ind_excluido=1)
        self.fields['cod_area_conhecimento'].widget.attrs['onChange'] = 'selectTreinamento(this)'

    class Meta:
        model = Treinamento
        fields = ('nome', 'cod_area_conhecimento')
        labels = {
            'nome' : 'Nome',
            'cod_area_conhecimento': 'Área de conhecimento',
        }

class TipoTreinamentoForm(forms.ModelForm):

    class Meta:
        model = Tipo_Treinamento
        fields = ('nome', )
        labels = {
            'nome' : 'Nome'
        }
