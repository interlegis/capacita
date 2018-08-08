from django.db import models
from django.utils import timezone

class Area_Conhecimento(models.Model):
    cod_area_conhecimento = models.AutoField(primary_key=True)
    txt_descricao = models.CharField(max_length=200)
    ind_excluido = models.DecimalField(default=0,decimal_places=0, max_digits=2)

    class Meta:
        db_table = 'Area_Conhecimento'

    def __str__(self):
        return self.txt_descricao

class Sub_Area_Conhecimento(models.Model):
    cod_sub_area_conhecimento = models.AutoField(primary_key=True)
    cod_area_conhecimento = models.ForeignKey('Area_Conhecimento', on_delete=models.CASCADE)
    txt_descricao = models.CharField(max_length=200)
    ind_excluido = models.DecimalField(default=0, decimal_places=0, max_digits=2)

    class Meta:
        db_table = 'Sub_Area_Conhecimento'

    def __str__(self):
        return self.txt_descricao

class Prioridade(models.Model):
    cod_prioridade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    class Meta:
        db_table = 'Prioridade'

class Orgao(models.Model):
    cod_orgao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Orgao'
    
class Avaliacao(models.Model):
    cod_avaliacao = models.AutoField(primary_key=True)
    cod_necessidade = models.ForeignKey('Necessidade', on_delete=models.CASCADE)
    # cod_acao = models.ForeignKey('Acao', on_delete=models.CASCADE)
    # cod_modalidade = models.DecimalField(decimal_places=0, max_digits=2)
    valor_custo = models.DecimalField(decimal_places=2, max_digits=17)
    ind_excluido = models.DecimalField(default=0,decimal_places=0, max_digits=2)


    class Meta:
        db_table = 'Avaliacao'

class Turno(models.Model):
    cod_turno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):              
        return self.nome

    class Meta:
        db_table = 'Turno'

class Mes(models.Model):
    cod_mes = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Mes'

class Nivel(models.Model):
    cod_nivel = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    class Meta:
        db_table = 'Nivel'

class Iniciativa(models.Model):
    cod_iniciativa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    class Meta:
        db_table = 'Iniciativa'

    def __str__(self):
        return self.nome

class Necessidade(models.Model):
    cod_necessidade = models.AutoField(primary_key=True)
    txt_descricao = models.CharField(max_length=200)
    cod_plano_capacitacao = models.ForeignKey('Plano_Capacitacao', on_delete=models.CASCADE)
    cod_iniciativa = models.ForeignKey('Iniciativa', on_delete=models.CASCADE)
    cod_prioridade =models.ForeignKey('Prioridade', on_delete=models.CASCADE)
    qtd_servidor = models.DecimalField(decimal_places=0, max_digits=6)
    cod_sub_area_conhecimento = models.ForeignKey('Sub_Area_Conhecimento', on_delete=models.CASCADE)
    cod_nivel = models.ForeignKey('Nivel', on_delete=models.CASCADE)
    hor_duracao = models.DecimalField(decimal_places=0, max_digits=2)
    cod_turno = models.ForeignKey('Turno', on_delete=models.CASCADE)
    cod_mes = models.ForeignKey('Mes', on_delete=models.CASCADE)
    ind_excluido = models.DecimalField(default=0,decimal_places=0, max_digits=2)

    class Meta:
        db_table = 'Necessidade'    

class Permissao(models.Model):
    cod_permissao = models.AutoField(primary_key=True)
    cod_tipo_plano_capacitacao = models.ForeignKey('Tipo_Plano_Capacitacao', on_delete=models.CASCADE)
    ano_plano_capacitacao = models.DecimalField(decimal_places=0, max_digits=4, null= False)
    cod_secretaria = models.ForeignKey('Secretaria', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Permissao'

class Secretaria(models.Model):
    cod_secretaria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    class Meta:
        db_table = 'Secretaria'
    
class Plano_Capacitacao(models.Model):
    cod_plano_capacitacao = models.AutoField(primary_key=True)
    cod_orgao = models.ForeignKey('Orgao', on_delete=models.CASCADE)
    cod_tipo_plano_capacitacao = models.ForeignKey('Tipo_Plano_Capacitacao', on_delete=models.CASCADE)
    situacao = models.CharField(max_length=200)
    qtd_servidores_efetivos = models.IntegerField()
    qtd_servidores_comissionados = models.IntegerField()
    ano_plano_capacitacao = models.DecimalField(decimal_places=0, max_digits=4, null= False)
    ind_excluido = models.DecimalField(default=0,decimal_places=0, max_digits=2)

    class Meta:
        db_table = 'Plano_Capacitacao' 

class Tipo_Plano_Capacitacao(models.Model):
    cod_tipo_plano_capacitacao = models.AutoField(primary_key=True)
    sgl_tipo_plano_capacitacao = models.CharField(max_length = 6, null=False)
    nome_tipo_plano_capacitacao = models.CharField(max_length= 200, null=False)
    ind_excluido = models.DecimalField(default=0,decimal_places=0, max_digits=2)

    def __str__(self):
        return self.nome_tipo_plano_capacitacao

    class Meta:
        db_table = 'Tipo_Plano_Capacitacao' 

    

