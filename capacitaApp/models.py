from django.db import models

from django.contrib.auth.models import User
from plano.models import Plano_Capacitacao
from orgao.models import Orgao
from areas.models import Area_Conhecimento
from tipo_treinamento.models import Tipo_Treinamento
from treinamento.models import Treinamento
from objetivos.models import Objetivo_Treinamento
from modalidade.models import Modalidade_Treinamento

from django import forms

class Nivel(models.Model):
    cod_nivel = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200,unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'nivel'
        ordering = ['nome']

class Permissao(models.Model):
    cod_permissao = models.AutoField(primary_key=True)
    ano_plano_capacitacao = models.DecimalField(max_digits=4, decimal_places=0)
    cod_orgao = models.ForeignKey('orgao.Orgao', models.DO_NOTHING)

    class Meta:
        db_table = 'permissao'


class Prioridade(models.Model):
    cod_prioridade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, unique=True)
    ind_excluido = models.NullBooleanField(null = False, default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'prioridade'
        ordering = ['nome']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orgao = models.ForeignKey(Orgao, null=True, on_delete=models.CASCADE, related_name='orgao_id') #Orgao atual
    orgaos_vinculados = models.ManyToManyField(Orgao, related_name='orgaos_vinculados')
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
