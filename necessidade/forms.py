from django import forms
from django.contrib.auth.models import User, Group
from capacitaApp.models import *
from necessidade.models import *


class NecessidadeForm(forms.ModelForm):
    # Adicionando forms
    justificativa = forms.CharField(widget=forms.Textarea)
    hor_duracao = forms.CharField(required=False)
    treinamento = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        emptyField = [('', '---------')]
        treinamento_outro = [('-1', '* Outro (especificar) *')]
        super(NecessidadeForm, self).__init__(*args, **kwargs)

        # treinamento
        treinamentos = emptyField + [(treinamento.pk, treinamento) for treinamento in Treinamento.objects.all().exclude(cod_treinamento = -1)] + treinamento_outro
        self.fields['treinamento'] = forms.ChoiceField(choices= treinamentos)
        self.fields['treinamento'].widget.attrs['onChange'] = 'selectSugestao(this)'

        # areas_conhecimento
        self.fields['cod_area_conhecimento'].queryset = Area_Conhecimento.objects.all().exclude(ind_excluido=1)
        self.fields['cod_area_conhecimento'].widget.attrs['onChange'] = 'selectTreinamento(this)'

        # objetivo_treinamento
        self.fields['cod_objetivo_treinamento'].queryset = Objetivo_Treinamento.objects.all()

        # modalidade
        self.fields['cod_modalidade'].queryset = Modalidade_Treinamento.objects.all()

        # niveis
        self.fields['cod_nivel'].queryset = Nivel.objects.all()

        # tipos_treinamento
        self.fields['cod_tipo_treinamento'].queryset = Tipo_Treinamento.objects.all()


    class Meta:
        model = Necessidade
        fields = ('qtd_servidor','hor_duracao','cod_nivel','cod_modalidade', 'cod_prioridade', 'cod_tipo_treinamento', 'justificativa', 'treinamento', 'cod_area_conhecimento', 'cod_objetivo_treinamento')
        labels = {
            'qtd_servidor' : 'Quantidade de Servidores Efetivos',
            'hor_duracao'  : 'Hora de duração',
            'cod_tipo_treinamento' : 'Tipo de Treinamento',
            'justificativa' : 'Justificativa',
            'cod_modalidade' : 'Modalidade de Treinamento',
            'cod_nivel' : 'Nível',
            'cod_prioridade' : 'Prioridade',
            'treinamento': 'Treinamento',
            'cod_area_conhecimento': 'Área de conhecimento',
            'cod_objetivo_treinamento': "Objetivo de Treinamento"
        }
