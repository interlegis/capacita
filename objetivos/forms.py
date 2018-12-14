from django import forms
from django.contrib.auth.models import User, Group
from .models import *

class ObjetivoTreinamentoForm(forms.ModelForm):

    class Meta:
        model = Objetivo_Treinamento
        fields = ('nome', )
        labels = {
            'nome' : 'Nome'
        }
