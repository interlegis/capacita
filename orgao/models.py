from django.db import models

class Orgao(models.Model):
    cod_orgao = models.AutoField(primary_key=True)
    cod_superior = models.ForeignKey('Orgao', models.DO_NOTHING, null = True, blank=True)
    nome = models.CharField(max_length=30, unique=True)
    descricao = models.CharField(max_length=500)
    ind_excluido = models.BooleanField( default=False)
    nivel = models.IntegerField( default=-1)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'orgao'
        ordering = ['nome']