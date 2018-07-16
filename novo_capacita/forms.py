# -*- coding: utf-8 -*-

from django import forms
from .models import *

class NecessidadeForm(forms.ModelForm):

    class Meta:
        model = Necessidade
        fields = ('txt_descricao','qtd_servidor','hor_duracao','cod_iniciativa','cod_mes','cod_nivel','cod_plano_capacitacao','cod_area_conhecimento','cod_prioridade','cod_turno')
        labels = {
            'txt_descricao': 'Descrição',
            'qtd_servidor' : 'Quantidade de Servidores Efetivos',
            'hor_duracao'  : 'Hora de duração',
            'cod_area_conhecimento' : 'Área de Conhecimento',
            'cod_iniciativa' : "Iniciativa",
            'cod_mes' : 'Mês',
            'cod_nivel' : 'Nível',
            'cod_turno' : 'Turnos',
            'cod_plano_capacitacao' : 'Plano de Capacitação',
            'cod_prioridade' : 'Prioridade'
        }

class PlanoForm(forms.ModelForm):

    class Meta:
        model = Plano_Capacitacao
        fields = ('cod_orgao', 'cod_tipo_plano_capacitacao', 'ano_plano_capacitacao','situacao', 'qtd_servidores_efetivos', 'qtd_servidores_comissionados')
        labels = {
            'cod_orgao' : 'Órgão'
        }