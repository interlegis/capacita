from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django import forms

class Area_Conhecimento(models.Model):
    cod_area_conhecimento = models.AutoField(primary_key=True)
    txt_descricao = models.CharField(max_length=200)
    ind_excluido = models.DecimalField(default=0,max_digits=2, decimal_places=0)

    def __str__(self):
        return self.txt_descricao

    class Meta:
        managed = False
        db_table = 'Area_Conhecimento'


class Orgao(models.Model):
    cod_orgao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Orgao'


class Avaliacao(models.Model):
    cod_avaliacao = models.AutoField(primary_key=True)
    valor_custo = models.DecimalField(max_digits=17, decimal_places=2)
    ind_excluido = models.DecimalField(default=0,max_digits=2, decimal_places=0)
    cod_necessidade = models.ForeignKey('Necessidade', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Avaliacao'


class Iniciativa(models.Model):
    cod_iniciativa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Iniciativa'


class Mes(models.Model):
    cod_mes = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Mes'

class Sub_Area_Conhecimento(models.Model):
    cod_sub_area_conhecimento = models.AutoField(primary_key=True)
    txt_descricao = models.CharField(max_length=200)
    ind_excluido = models.DecimalField(default=0,max_digits=2, decimal_places=0)
    cod_area_conhecimento = models.ForeignKey(Area_Conhecimento, models.DO_NOTHING)

    def __str__(self):
        return self.txt_descricao

    class Meta:
        managed = False
        db_table = 'Sub_Area_Conhecimento'

class Curso(models.Model):
    cod_curso = models.AutoField(primary_key=True)
    sub_area = models.ForeignKey(Sub_Area_Conhecimento, models.DO_NOTHING)
    nome = models.CharField(max_length=900)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Curso'

class Modalidade_Treinamento(models.Model):
    cod_modalidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    ind_excluido = models.NullBooleanField(null = False, default=False) 

    def __str__(self):
        return self.nome
    
    class Meta:
        managed = False
        db_table = 'Modalidade_Treinamento'

class Evento(models.Model):
    cod_evento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    ind_excluido = models.NullBooleanField(null = False, default=False) 

    def __str__(self):
        return self.nome
    
    class Meta:
        managed = False
        db_table = 'Evento'

class Necessidade(models.Model):
    cod_necessidade = models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, models.DO_NOTHING, null=True)
    txt_descricao = models.CharField(max_length=200, null=True)
    qtd_servidor = models.DecimalField(max_digits=6, decimal_places=0)
    hor_duracao = models.DecimalField(max_digits=2, decimal_places=0)
    cod_evento = models.ForeignKey('Evento', models.DO_NOTHING, null=True)
    ind_excluido = models.DecimalField(default=0,max_digits=2, decimal_places=0)
    custo = models.DecimalField(max_digits=6, decimal_places=2, default=100)
    cod_modalidade = models.ForeignKey('Modalidade_Treinamento', models.DO_NOTHING)
    cod_tipo = models.ForeignKey('Tipo_Plano_Capacitacao', models.DO_NOTHING)
    cod_nivel = models.ForeignKey('Nivel', models.DO_NOTHING)
    cod_usuario = models.ForeignKey(User,models.DO_NOTHING)
    cod_plano_capacitacao = models.ForeignKey('Plano_Capacitacao', models.DO_NOTHING)
    cod_prioridade = models.ForeignKey('Prioridade', models.DO_NOTHING)
    cod_sub_area_conhecimento = models.ForeignKey('Sub_Area_Conhecimento', models.DO_NOTHING)
    aprovado = models.NullBooleanField(null = False, default=False) 
    justificativa = models.CharField(max_length=300)

    def __str__(self):
        return self.txt_descricao

    class Meta:
        managed = False
        db_table = 'Necessidade'


class Nivel(models.Model):
    cod_nivel = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Nivel'


class Permissao(models.Model):
    cod_permissao = models.AutoField(primary_key=True)
    ano_plano_capacitacao = models.DecimalField(max_digits=4, decimal_places=0)
    cod_secretaria = models.ForeignKey('Secretaria', models.DO_NOTHING)
    cod_tipo_plano_capacitacao = models.ForeignKey('Tipo_Plano_Capacitacao', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Permissao'


class Plano_Capacitacao(models.Model):
    cod_plano_capacitacao = models.AutoField(primary_key=True)
    qtd_servidores_efetivos = models.IntegerField()
    qtd_servidores_comissionados = models.IntegerField()
    data_inicio = models.DateField(null=True)
    data_fim = models.DateField(null=True)
    ano_plano_capacitacao = models.DecimalField(max_digits=4, decimal_places=0)
    ind_excluido = models.DecimalField(default=0,max_digits=2, decimal_places=0)
    plano_habilitado = models.NullBooleanField(null = False)

    def __str__(self):
        return str(str(self.ano_plano_capacitacao))

    class Meta:
        managed = False
        db_table = 'Plano_Capacitacao'


class Prioridade(models.Model):
    cod_prioridade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Prioridade'


class Secretaria(models.Model):
    cod_secretaria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Secretaria'


class Tipo_Plano_Capacitacao(models.Model):
    cod_tipo_plano_capacitacao = models.AutoField(primary_key=True)
    sgl_tipo_plano_capacitacao = models.CharField(max_length=6)
    nome_tipo_plano_capacitacao = models.CharField(max_length=200)
    ind_excluido = models.DecimalField(default=0,null = True, max_digits=2, decimal_places=0)

    def __str__(self):
        return self.nome_tipo_plano_capacitacao

    class Meta:
        managed = False
        db_table = 'Tipo_Plano_Capacitacao'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCasNgProxygrantingticket(models.Model):
    session_key = models.CharField(max_length=255, blank=True, null=True)
    pgtiou = models.CharField(max_length=255, blank=True, null=True)
    pgt = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_cas_ng_proxygrantingticket'
        unique_together = (('session_key', 'user'),)


class DjangoCasNgSessionticket(models.Model):
    session_key = models.CharField(max_length=255)
    ticket = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'django_cas_ng_sessionticket'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orgao = models.ForeignKey(Orgao, null=True, on_delete=models.CASCADE)
    permissao_necessidade = models.NullBooleanField(null = True, default=False)



    

