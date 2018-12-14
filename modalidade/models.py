from django.db import models

class Modalidade_Treinamento(models.Model):
    cod_modalidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'modalidade_treinamento'
        ordering = ['nome']
