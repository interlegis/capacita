# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novo_capacita', '0002_auto_20180625_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area_Conhecimento',
            fields=[
                ('cod_area_conhecimento', models.AutoField(serialize=False, primary_key=True)),
                ('txt_descricao', models.CharField(max_length=200)),
                ('ind_excluido', models.DecimalField(default=0, max_digits=2, decimal_places=0)),
            ],
            options={
                'db_table': 'Area_Conhecimento',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('cod_avaliacao', models.AutoField(serialize=False, primary_key=True)),
                ('valor_custo', models.DecimalField(max_digits=17, decimal_places=2)),
                ('ind_excluido', models.DecimalField(default=0, max_digits=2, decimal_places=0)),
            ],
            options={
                'db_table': 'Avaliacao',
            },
        ),
        migrations.CreateModel(
            name='Iniciativa',
            fields=[
                ('cod_iniciativa', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Iniciativa',
            },
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('cod_mes', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Mes',
            },
        ),
        migrations.CreateModel(
            name='Necessidade',
            fields=[
                ('cod_necessidade', models.AutoField(serialize=False, primary_key=True)),
                ('txt_descricao', models.CharField(max_length=200)),
                ('qtd_servidor', models.DecimalField(max_digits=6, decimal_places=0)),
                ('hor_duracao', models.DecimalField(max_digits=2, decimal_places=0)),
                ('ind_excluido', models.DecimalField(default=0, max_digits=2, decimal_places=0)),
                ('cod_area_conhecimento', models.ForeignKey(to='novo_capacita.Area_Conhecimento')),
                ('cod_iniciativa', models.ForeignKey(to='novo_capacita.Iniciativa')),
                ('cod_mes', models.ForeignKey(to='novo_capacita.Mes')),
            ],
            options={
                'db_table': 'Necessidade',
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('cod_nivel', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Nivel',
            },
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('cod_orgao', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Orgao',
            },
        ),
        migrations.CreateModel(
            name='Permissao',
            fields=[
                ('cod_permissao', models.AutoField(serialize=False, primary_key=True)),
                ('ano_plano_capacitacao', models.DecimalField(max_digits=4, decimal_places=0)),
            ],
            options={
                'db_table': 'Permissao',
            },
        ),
        migrations.CreateModel(
            name='Plano_Capacitacao',
            fields=[
                ('cod_plano_capacitacao', models.AutoField(serialize=False, primary_key=True)),
                ('ano_plano_capacitacao', models.DecimalField(max_digits=4, decimal_places=0)),
                ('ind_excluido', models.DecimalField(default=0, max_digits=2, decimal_places=0)),
                ('cod_orgao', models.ForeignKey(to='novo_capacita.Orgao')),
            ],
            options={
                'db_table': 'Plano_Capacitacao',
            },
        ),
        migrations.CreateModel(
            name='Prioridade',
            fields=[
                ('cod_prioridade', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Prioridade',
            },
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('cod_secretaria', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Secretaria',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Plano_Capacitacao',
            fields=[
                ('cod_tipo_plano_capacitacao', models.AutoField(serialize=False, primary_key=True)),
                ('sgl_tipo_plano_capacitacao', models.CharField(max_length=6)),
                ('nom_tipo_plano_capacitacao', models.CharField(max_length=6)),
                ('ind_excluido', models.DecimalField(default=0, max_digits=2, decimal_places=0)),
            ],
            options={
                'db_table': 'Tipo_Plano_Capacitacao',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('cod_turno', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Turno',
            },
        ),
        migrations.DeleteModel(
            name='Acao',
        ),
        migrations.AddField(
            model_name='plano_capacitacao',
            name='cod_tipo_plano_capacitacao',
            field=models.ForeignKey(to='novo_capacita.Tipo_Plano_Capacitacao'),
        ),
        migrations.AddField(
            model_name='permissao',
            name='cod_secretaria',
            field=models.ForeignKey(to='novo_capacita.Secretaria'),
        ),
        migrations.AddField(
            model_name='permissao',
            name='cod_tipo_plano_capacitacao',
            field=models.ForeignKey(to='novo_capacita.Tipo_Plano_Capacitacao'),
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_nivel',
            field=models.ForeignKey(to='novo_capacita.Nivel'),
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_plano_capacitacao',
            field=models.ForeignKey(to='novo_capacita.Plano_Capacitacao'),
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_prioridade',
            field=models.ForeignKey(to='novo_capacita.Prioridade'),
        ),
        migrations.AddField(
            model_name='necessidade',
            name='cod_turno',
            field=models.ForeignKey(to='novo_capacita.Turno'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='cod_necessidade',
            field=models.ForeignKey(to='novo_capacita.Necessidade'),
        ),
    ]
