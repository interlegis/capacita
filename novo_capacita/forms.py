# -*- coding: utf-8 -*-

from django import forms
from .models import *

class NecessidadeForm(forms.ModelForm):
    
    class Meta:
        model = Necessidade
        fields = ('txt_descricao','qtd_servidor','hor_duracao','cod_area_conhecimento','cod_iniciativa','cod_mes','cod_nivel','cod_plano_capacitacao','cod_prioridade','cod_turno')
        labels = {
            'txt_descricao': 'Descrição',
            'qtd_servidor' : 'Quantidade de Servidores Efetivos',
            'hor_duracao'  : 'Hora de duração',
            
        }