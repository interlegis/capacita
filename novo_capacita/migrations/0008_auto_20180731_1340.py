# Generated by Django 2.0.7 on 2018-07-31 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novo_capacita', '0007_auto_20180731_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sub_area_conhecimento',
            old_name='cod_area_conhecimento_id',
            new_name='cod_area_conhecimento',
        ),
    ]
