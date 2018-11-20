# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group
from .models import *

class NecessidadeForm(forms.ModelForm):
    emptyField = [('', '---------')]
    treinamento_outro = [('-1', '* Outro (especificar) *')]
    treinamentos = emptyField + [(treinamento.pk, treinamento) for treinamento in Treinamento.objects.all().exclude(cod_treinamento = -1)] + treinamento_outro
    areas_conhecimento = emptyField + [(area.pk, area) for area in Area_Conhecimento.objects.all()]
    justificativa = forms.CharField(widget=forms.Textarea)
    objetivos = emptyField + [(objetivo.pk, objetivo) for objetivo in Objetivo_Treinamento.objects.all()]
    objetivo_treinamento = forms.ChoiceField(
                            choices= objetivos,
                            )
    treinamento = forms.ChoiceField(
                            choices= treinamentos,
                            widget = forms.Select(attrs = {
                                'onclick': "selectSugestao(this);",
                            }))
    area_conhecimento = forms.ChoiceField(
                                choices= areas_conhecimento,
                                widget = forms.Select(attrs = {
                                    'onclick': "selectTreinamento(this);",
                                }))

    class Meta:
        model = Necessidade
        fields = ('qtd_servidor','hor_duracao','cod_nivel','cod_modalidade', 'cod_prioridade', 'justificativa', 'cod_evento', 'treinamento', 'area_conhecimento', 'objetivo_treinamento')
        labels = {
            'qtd_servidor' : 'Quantidade de Servidores Efetivos',
            'hor_duracao'  : 'Hora de duração',
            'cod_evento' : 'Evento',
            'cod_tipo' : 'Tipo de Modalidade',
            'justificativa' : 'Justificativa',
            'cod_modalidade' : 'Modalidade de Treinamento',
            'cod_nivel' : 'Nível',
            'cod_prioridade' : 'Prioridade',
            'treinamento': 'Treinamento',
            'area_conhecimento': 'Área de conhecimento',
            'objetivo_treinamento': "Objetivo de Treinamento"
        }

class PlanoForm(forms.ModelForm):

    class Meta:
        model = Plano_Capacitacao
        fields = ('ano_plano_capacitacao', 'plano_habilitado')

class OrgaoForm(forms.ModelForm):

    class Meta:
        model = Orgao
        fields = ('nome', )
        labels = {
            'nome' : 'Nome'
        }

class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ('nome', )
        labels = {
            'nome' : 'Nome'
        }

class ObjetivoTreinamentoForm(forms.ModelForm):

    class Meta:
        model = Objetivo_Treinamento
        fields = ('nome', )
        labels = {
            'nome' : 'Nome'
        }

class TipoTreinamentoForm(forms.ModelForm):

    class Meta:
        model = Tipo_Treinamento
        fields = ('nome', )
        labels = {
            'nome' : 'Nome'
        }

class TreinamentoForm(forms.ModelForm):

    class Meta:
        model = Treinamento
        fields = ('nome', )
        labels = {
            'nome' : 'Nome'
        }

class UserForm(forms.ModelForm):

    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    is_staff = False
    is_active = True
    is_superuser = False

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
        # labels = {
        #     'username' : 'Login'
        # }

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('orgao', )

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('id', )

class TreinamentoForm(forms.ModelForm):
    class Meta:
        model = Treinamento
        fields = ('cod_treinamento', 'cod_area_conhecimento', 'nome')

class ModalidadeForm(forms.ModelForm):

    class Meta:
        model = Modalidade_Treinamento
        fields = ('cod_modalidade', 'nome')

class AreaConhecimentoForm(forms.ModelForm):

    class Meta:
        model = Area_Conhecimento
        fields = ('txt_descricao',) 
