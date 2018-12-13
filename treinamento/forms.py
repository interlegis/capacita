# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group
from capacitaApp.models import *

class TreinamentoForm(forms.ModelForm):

    class Meta:
        model = Treinamento
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
