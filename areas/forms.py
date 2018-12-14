from django import forms
from django.contrib.auth.models import User, Group
from capacitaApp.models import *


class AreaConhecimentoForm(forms.ModelForm):

    class Meta:
        model = Area_Conhecimento
        fields = ('cod_area_conhecimento', 'txt_descricao')

class AreaConhecimentoForm(forms.ModelForm):

    class Meta:
        model = Area_Conhecimento
        fields = ('txt_descricao',)
