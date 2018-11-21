from django.db import models
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django import forms

class Orgao(models.Model):
    cod_orgao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'orgao'

class Area_Conhecimento(models.Model):
    cod_area_conhecimento = models.AutoField(primary_key=True)
    txt_descricao = models.CharField(max_length=200, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.txt_descricao

    class Meta:
        db_table = 'area_conhecimento'
        ordering = ['txt_descricao']

class Tipo_Treinamento(models.Model):
    cod_tipo_treinamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=900, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tipo_treinamento'
        ordering = ['nome']

class Treinamento(models.Model):
    cod_treinamento = models.AutoField(primary_key=True)
    cod_area_conhecimento = models.ForeignKey('Area_Conhecimento', models.DO_NOTHING, default='0')
    nome = models.CharField(max_length=900, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'treinamento'
        ordering = ['nome']

class Tipo_Treinamento(models.Model):
    cod_tipo_treinamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=900, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tipo_treinamento'

class Objetivo_Treinamento(models.Model):
    cod_objetivo_treinamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'objetivo_treinamento'
        ordering = ['nome']

class Modalidade_Treinamento(models.Model):
    cod_modalidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'modalidade_treinamento'
        ordering = ['nome']

class Evento(models.Model):
    cod_evento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'evento'
        ordering = ['nome']

class Necessidade(models.Model):
    cod_necessidade = models.AutoField(primary_key=True)
    cod_plano_capacitacao = models.ForeignKey('plano_capacitacao', models.DO_NOTHING)
    cod_area_conhecimento = models.ForeignKey('area_conhecimento', models.DO_NOTHING)
    cod_treinamento = models.ForeignKey('treinamento', models.DO_NOTHING, default='-1')
    txt_descricao = models.CharField(max_length=200, null=True)
    cod_evento = models.ForeignKey('evento', models.DO_NOTHING, null=True)
    cod_modalidade = models.ForeignKey('modalidade_treinamento', models.DO_NOTHING)
    cod_nivel = models.ForeignKey('nivel', models.DO_NOTHING)
    hor_duracao = models.DecimalField(max_digits=3, decimal_places=0, validators=[MinValueValidator(0)])
    cod_prioridade = models.ForeignKey('prioridade', models.DO_NOTHING)
    qtd_servidor = models.DecimalField(max_digits=6, decimal_places=0, validators=[MinValueValidator(0)])
    cod_objetivo_treinamento = models.ForeignKey('objetivo_treinamento', models.DO_NOTHING)
    justificativa = models.CharField(max_length=300)
    aprovado = models.NullBooleanField(null = False, default=False)
    cod_usuario = models.ForeignKey(User,models.DO_NOTHING)
    cod_orgao = models.ForeignKey('orgao', models.DO_NOTHING)
    cod_tipo_treinamento = models.ForeignKey('tipo_treinamento', models.DO_NOTHING)

    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.txt_descricao

    class Meta:
        db_table = 'necessidade'
        ordering = ['cod_area_conhecimento','cod_treinamento']


class Nivel(models.Model):
    cod_nivel = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200,unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'nivel'


class Permissao(models.Model):
    cod_permissao = models.AutoField(primary_key=True)
    ano_plano_capacitacao = models.DecimalField(max_digits=4, decimal_places=0)
    cod_orgao = models.ForeignKey('orgao', models.DO_NOTHING)

    class Meta:
        db_table = 'permissao'


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

class Prioridade(models.Model):
    cod_prioridade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'prioridade'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orgao = models.ForeignKey(Orgao, null=True, on_delete=models.CASCADE)
    permissao_necessidade = models.NullBooleanField(null = True, default=False)

    class Meta:
        db_table = 'capacita_profile'

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
