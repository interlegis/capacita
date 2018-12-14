from django.db import models

from orgao.models import Orgao
from areas.models import Area_Conhecimento
from django.contrib.auth.models import User

class Sugestao(models.Model):
    cod_sugestao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    cod_orgao = models.ForeignKey(Orgao, null=True, on_delete=models.CASCADE, db_column='cod_orgao')
    cod_area_conhecimento = models.ForeignKey('areas.Area_Conhecimento', null=True, on_delete=models.CASCADE, db_column='cod_area_conhecimento')
    observacoes = models.CharField(max_length=200)
    cod_usuario = models.ForeignKey(User, null=True, on_delete= models.CASCADE, db_column='cod_usuario')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'sugestao'
        ordering = ['nome']
