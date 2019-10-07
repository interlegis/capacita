# Generated by Django 2.2.6 on 2019-10-03 20:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plano', '0001_initial'),
        ('orgao', '0001_initial'),
        ('capacitaApp', '0001_initial'),
        ('areas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treinamento', '0001_initial'),
        ('tipo_treinamento', '0001_initial'),
        ('modalidade', '0001_initial'),
        ('objetivos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Necessidade_Orgao',
            fields=[
                ('cod_necessidade_orgao', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=False)),
                ('importado', models.BooleanField(default=False)),
                ('cod_orgao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgao.Orgao')),
                ('cod_plano_capacitacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.Plano_Capacitacao')),
            ],
            options={
                'db_table': 'necessidade_orgao',
            },
        ),
        migrations.CreateModel(
            name='Necessidade',
            fields=[
                ('cod_necessidade', models.AutoField(primary_key=True, serialize=False)),
                ('txt_descricao', models.CharField(max_length=200, null=True)),
                ('hor_duracao', models.DecimalField(decimal_places=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('qtd_servidor', models.DecimalField(decimal_places=0, max_digits=6, validators=[django.core.validators.MinValueValidator(1)])),
                ('justificativa', models.CharField(max_length=300)),
                ('ementa', models.TextField()),
                ('aprovado', models.BooleanField(default=True)),
                ('ind_excluido', models.BooleanField(default=False)),
                ('treinamento_externo', models.BooleanField()),
                ('valor_estimado', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('cod_area_conhecimento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='areas.Area_Conhecimento')),
                ('cod_modalidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modalidade.Modalidade_Treinamento')),
                ('cod_necessidade_orgao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='necessidade.Necessidade_Orgao')),
                ('cod_nivel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Nivel')),
                ('cod_objetivo_treinamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='objetivos.Objetivo_Treinamento')),
                ('cod_orgao_origem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgao.Orgao')),
                ('cod_prioridade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='capacitaApp.Prioridade')),
                ('cod_tipo_treinamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tipo_treinamento.Tipo_Treinamento')),
                ('cod_treinamento', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.DO_NOTHING, to='treinamento.Treinamento')),
                ('cod_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'necessidade',
                'ordering': ['cod_area_conhecimento', 'cod_treinamento', 'cod_modalidade', 'cod_nivel', 'cod_tipo_treinamento', 'cod_prioridade', 'cod_objetivo_treinamento'],
            },
        ),
    ]
