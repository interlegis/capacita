# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group
from .models import *

class NecessidadeForm(forms.ModelForm):

    curso = forms.ChoiceField(required=False)
    justificativa = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Necessidade
        fields = ('qtd_servidor','hor_duracao','cod_iniciativa','cod_mes','cod_nivel','cod_sub_area_conhecimento','cod_prioridade','cod_turno', 'justificativa', 'custo')
        labels = {
            'qtd_servidor' : 'Quantidade de Servidores Efetivos',
            'hor_duracao'  : 'Hora de duração',
            'cod_sub_area_conhecimento' : 'Sub-Área de Conhecimento',
            'cod_iniciativa' : "Iniciativa",
            'cod_mes' : 'Mês',
            'justificativa' : 'Justificativa',
            'custo' : 'Custo',
            'cod_nivel' : 'Nível',
            'cod_turno' : 'Turnos',
            'cod_prioridade' : 'Prioridade'
        }
    
    def __init__(self, *args, **kwargs):
        super(NecessidadeForm, self).__init__(*args, **kwargs)
        self.fields['curso'].widget.attrs\
            .update({
                'id' : 'nome_curso_form'
            })

class PlanoForm(forms.ModelForm):

    class Meta:
        model = Plano_Capacitacao
        fields = ('cod_orgao', 'cod_tipo_plano_capacitacao', 'ano_plano_capacitacao','situacao', 'qtd_servidores_efetivos', 'qtd_servidores_comissionados', 'plano_habilitado')
        labels = {
            'cod_orgao' : 'Órgão'
        }

class OrgaoForm(forms.ModelForm):

    class Meta:
        model = Orgao
        fields = ('nome', )
        labels = {
            'nome' : 'Nome'
        }

class TipoForm(forms.ModelForm):

    class Meta:
        model = Tipo_Plano_Capacitacao
        fields = ('sgl_tipo_plano_capacitacao', 'nome_tipo_plano_capacitacao', )

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

class SubAreaForm(forms.ModelForm):

    class Meta:
        model = Sub_Area_Conhecimento
        fields = ('cod_sub_area_conhecimento', 'cod_area_conhecimento', 'txt_descricao')