from django.db import models

class Area_Conhecimento(models.Model):
    cod_area_conhecimento = models.AutoField(primary_key=True)
    txt_descricao = models.CharField(max_length=200, unique=True)
    ind_excluido = models.BooleanField( default=False)

    def __str__(self):
        return self.txt_descricao

    class Meta:
        db_table = 'area_conhecimento'
        ordering = ['txt_descricao']
