# Generated by Django 4.0.1 on 2022-02-02 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCL',
            new_name='ClothesCL',
        ),
        migrations.AlterModelOptions(
            name='clothescl',
            options={'verbose_name': 'Одежда', 'verbose_name_plural': 'Одежды'},
        ),
    ]
