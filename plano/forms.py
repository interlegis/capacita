# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Group
from .models import *

class PlanoForm(forms.ModelForm):

    class Meta:
        model = Plano_Capacitacao
        fields = ('ano_plano_capacitacao', 'plano_habilitado')
