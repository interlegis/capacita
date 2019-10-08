# Generated by Django 2.2.6 on 2019-10-03 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('cod_orgao', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30, unique=True)),
                ('descricao', models.CharField(max_length=500)),
                ('ind_excluido', models.BooleanField(default=False)),
                ('cod_superior', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orgao.Orgao')),
            ],
            options={
                'db_table': 'orgao',
                'ordering': ['nome'],
            },
        ),
    ]
