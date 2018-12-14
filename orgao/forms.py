from django import forms
from django.contrib.auth.models import User, Group
from .models import *

class OrgaoForm(forms.ModelForm):

    class Meta:
        model = Orgao
        fields = ('nome', )
        labels = {
            'nome' : 'Nome'
        }
