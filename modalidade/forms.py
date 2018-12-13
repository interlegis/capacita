from django import forms
from django.contrib.auth.models import User, Group
from capacitaApp.models import *

class ModalidadeForm(forms.ModelForm):

    class Meta:
        model = Modalidade_Treinamento
        fields = ('cod_modalidade', 'nome')
