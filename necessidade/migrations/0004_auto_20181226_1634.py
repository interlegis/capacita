# Generated by Django 2.1.4 on 2018-12-26 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('necessidade', '0003_auto_20181220_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='necessidade',
            options={'ordering': ['cod_area_conhecimento']},
        ),
    ]
