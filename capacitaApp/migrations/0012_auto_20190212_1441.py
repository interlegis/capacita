# Generated by Django 2.1.4 on 2019-02-12 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacitaApp', '0011_auto_20190212_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgaopermissao',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='orgaopermissao',
            name='orgao',
        ),
        migrations.DeleteModel(
            name='OrgaoPermissao',
        ),
    ]