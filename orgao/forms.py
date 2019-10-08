from django import forms
from django.contrib.auth.models import User, Group
from .models import *

class OrgaoForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(OrgaoForm, self).__init__(*args, **kwargs)
        self.fields['cod_superior'].queryset = Orgao.objects.all()
        self.fields['nome'].widget.attrs['style'] = 'text-transform:uppercase;'
        self.fields['descricao'].widget.attrs['style'] = 'text-transform:uppercase;'

    class Meta:
        model = Orgao
        fields = ('nome', 'cod_superior', 'descricao')
        labels = {
            'nome' : 'Nome',
            'cod_superior': 'Orgao Superior',
            'descricao': 'Descrição'
        }
