# Generated by Django 2.1.3 on 2018-11-19 18:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('capacitaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area_Conhecimento',
            fields=[
                ('cod_area_conhecimento', models.AutoField(primary_key=True, serialize=False)),
                ('txt_descricao', models.CharField(max_length=200)),
                ('ind_excluido', models.NullBooleanField(default=False)),
            ],
            options={
                'db_table': 'area_conhecimento',
                'ordering': ['txt_descricao'],
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('cod_evento', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('ind_excluido', models.NullBooleanField(default=False)),
            ],
            options={
                'db_table': 'evento',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('cod_mes', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'mes',
            },
        ),
        migrations.CreateModel(
            name='Modalidade_Treinamento',
            fields=[
                ('cod_modalidade', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('ind_excluido', models.NullBooleanField(default=False)),
            ],
            options={
                'db_table': 'modalidade_treinamento',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Necessidade',
            fields=[
                ('cod_necessidade', models.AutoField(primary_key=True, serialize=False)),
                ('txt_descricao', models.CharField(max_length=200, null=True)),
                ('hor_duracao', models.DecimalField(decimal_places=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0)])),
                ('qtd_servidor', models.DecimalField(decimal_places=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('justificativa', models.CharField(max_length=300)),
                ('aprovado', models.NullBooleanField(default=False)),
                ('ind_excluido', models.NullBooleanField(default=False)),
                ('cod_area_conhecimento', models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Area_Conhecimento')),
                ('cod_evento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Evento')),
                ('cod_modalidade', models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Modalidade_Treinamento')),
            ],
            options={
                'db_table': 'necessidade',
                'ordering': ['cod_necessidade'],
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('cod_nivel', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('ind_excluido', models.NullBooleanField(default=False)),
            ],
            options={
                'db_table': 'nivel',
            },
        ),
        migrations.CreateModel(
            name='Objetivo_Treinamento',
            fields=[
                ('cod_objetivo_treinamento', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('ind_excluido', models.NullBooleanField(default=False)),
            ],
            options={
                'db_table': 'objetivo_treinamento',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('cod_orgao', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'orgao',
            },
        ),
        migrations.CreateModel(
            name='Permissao',
            fields=[
                ('cod_permissao', models.AutoField(primary_key=True, serialize=False)),
                ('ano_plano_capacitacao', models.DecimalField(decimal_places=0, max_digits=4)),
                ('cod_orgao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Orgao')),
            ],
            options={
                'db_table': 'permissao',
            },
        ),
        migrations.CreateModel(
            name='Plano_Capacitacao',
            fields=[
                ('cod_plano_capacitacao', models.AutoField(primary_key=True, serialize=False)),
                ('ano_plano_capacitacao', models.DecimalField(decimal_places=0, max_digits=4)),
                ('plano_habilitado', models.NullBooleanField()),
                ('ind_excluido', models.NullBooleanField(default=False)),
            ],
            options={
                'db_table': 'plano_capacitacao',
            },
        ),
        migrations.CreateModel(
            name='Prioridade',
            fields=[
                ('cod_prioridade', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('ind_excluido', models.NullBooleanField(default=False)),
            ],
            options={
                'db_table': 'prioridade',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissao_necessidade', models.NullBooleanField(default=False)),
                ('orgao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='capacitaApp.Orgao')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'capacita_profile',
            },
        ),
        migrations.CreateModel(
            name='Treinamento',
            fields=[
                ('cod_treinamento', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=900)),
                ('ind_excluido', models.NullBooleanField(default=False)),
                ('cod_area_conhecimento', models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Area_Conhecimento')),
            ],
            options={
                'db_table': 'treinamento',
                'ordering': ['nome'],
            },
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_nivel',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Nivel'),
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_objetivo_treinamento',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Objetivo_Treinamento'),
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_plano_capacitacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Plano_Capacitacao'),
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_prioridade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Prioridade'),
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_treinamento',
            field=models.ForeignKey(default='-1', on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Treinamento'),
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
