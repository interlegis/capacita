from django.db import models

class Tipo_Treinamento(models.Model):
    cod_tipo_treinamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=900, unique=True)
    ind_excluido = models.BooleanField( default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tipo_treinamento'
        ordering = ['nome']
