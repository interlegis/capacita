from django.db import models

class Objetivo_Treinamento(models.Model):
    cod_objetivo_treinamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, unique=True)
    ind_excluido = models.BooleanField( default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'objetivo_treinamento'
        ordering = ['nome']
