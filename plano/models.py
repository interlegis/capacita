from django.db import models

class Plano_Capacitacao(models.Model):
    cod_plano_capacitacao = models.AutoField(primary_key=True)
#    data_inicio = models.DateField(null=True)
 #   data_fim = models.DateField(null=True)
    ano_plano_capacitacao = models.DecimalField(max_digits=4, decimal_places=0, unique=True)
    plano_habilitado = models.NullBooleanField(null = False)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return str(str(self.ano_plano_capacitacao))

    class Meta:
        db_table = 'plano_capacitacao'
        ordering = ['ano_plano_capacitacao']
