# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group
from sugestao.models import *

class SugestaoForm(forms.ModelForm):

    class Meta:
        model = Sugestao
        fields = ('nome', 'cod_orgao', 'cod_area_conhecimento', 'observacoes')
