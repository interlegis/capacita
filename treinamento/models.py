from django.db import models
from areas.models import Area_Conhecimento

class Treinamento(models.Model):
    cod_treinamento = models.AutoField(primary_key=True)
    cod_area_conhecimento = models.ForeignKey('areas.Area_Conhecimento', models.DO_NOTHING, default='0')
    nome = models.CharField(max_length=900, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'treinamento'
        ordering = ['nome']
