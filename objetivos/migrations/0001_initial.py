# Generated by Django 2.1.4 on 2018-12-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objetivo_Treinamento',
            fields=[
                ('cod_objetivo_treinamento', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('ind_excluido', models.NullBooleanField(default=False)),
            ],
            options={
                'db_table': 'objetivo_treinamento',
                'ordering': ['nome'],
            },
        ),
    ]