from django import forms
from django.contrib.auth.models import User, Group
from .models import *

class OrgaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrgaoForm, self).__init__(*args, **kwargs)
        self.fields['cod_superior'].queryset = Orgao.objects.all()

    class Meta:
        model = Orgao
        fields = ('nome', 'cod_superior')
        labels = {
            'nome' : 'Nome',
            'cod_superior': 'Orgao Superior'
        }
