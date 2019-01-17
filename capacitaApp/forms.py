# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group
from .models import *

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('orgaos', )

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('id', )

class TreinamentoForm(forms.ModelForm):

    class Meta:
        model = Treinamento
        fields = ('cod_treinamento', 'cod_area_conhecimento', 'nome')
