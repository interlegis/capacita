# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('cod_acao', models.AutoField(serialize=False, primary_key=True)),
                ('text_descricao', models.CharField(max_length=200)),
                ('ind_excluido', models.DecimalField(max_digits=2, decimal_places=2)),
            ],
        ),
    ]
