# Generated by Django 2.1.4 on 2018-12-27 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacitaApp', '0004_auto_20181218_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='permissao_necessidade',
        ),
    ]