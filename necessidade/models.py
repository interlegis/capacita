from django.db import models
from django.core.validators import MinValueValidator

from plano.models import Plano_Capacitacao
from orgao.models import Orgao
from areas.models import Area_Conhecimento
from tipo_treinamento.models import Tipo_Treinamento
from treinamento.models import Treinamento
from objetivos.models import Objetivo_Treinamento
from modalidade.models import Modalidade_Treinamento
from capacitaApp.models import Nivel, Prioridade
from django.contrib.auth.models import User

class Necessidade(models.Model):
    cod_necessidade = models.AutoField(primary_key=True)
    cod_area_conhecimento = models.ForeignKey('areas.Area_conhecimento', models.DO_NOTHING)
    cod_treinamento = models.ForeignKey('treinamento.Treinamento', models.DO_NOTHING, default=-1)
    txt_descricao = models.CharField(max_length=200, null=True)
    cod_modalidade = models.ForeignKey('modalidade.Modalidade_Treinamento', models.DO_NOTHING)
    cod_nivel = models.ForeignKey('capacitaApp.nivel', models.DO_NOTHING)
    hor_duracao = models.DecimalField(max_digits=3, decimal_places=0, validators=[MinValueValidator(0)], null=True)
    cod_prioridade = models.ForeignKey('capacitaApp.Prioridade', models.DO_NOTHING)
    qtd_servidor = models.DecimalField(max_digits=6, decimal_places=0, validators=[MinValueValidator(0)])
    cod_objetivo_treinamento = models.ForeignKey('objetivos.Objetivo_Treinamento', models.DO_NOTHING)
    justificativa = models.CharField(max_length=300)
    aprovado = models.NullBooleanField(null = False, default=False)
    cod_usuario = models.ForeignKey(User, models.DO_NOTHING)
    cod_tipo_treinamento = models.ForeignKey('tipo_treinamento.Tipo_Treinamento', models.DO_NOTHING)
    cod_necessidade_orgao = models.ForeignKey('Necessidade_Orgao', models.DO_NOTHING)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.txt_descricao

    class Meta:
        db_table = 'necessidade'
        ordering = ['cod_area_conhecimento','cod_treinamento']

class Necessidade_Orgao(models.Model):
    cod_necessidade_orgao = models.AutoField(primary_key=True)
    cod_orgao = models.ForeignKey('orgao.Orgao', on_delete=models.CASCADE)
    cod_plano_capacitacao = models.ForeignKey('plano.Plano_Capacitacao', on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    importado = models.BooleanField(default=False)

    class Meta:
        db_table = 'necessidade_orgao'
