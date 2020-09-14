# Generated by Django 3.1.1 on 2020-09-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0004_auto_20200914_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='titulo',
        ),
        migrations.AddField(
            model_name='categoria',
            name='titulo',
            field=models.ManyToManyField(blank=True, related_name='categoria_titulo', to='cuenta.Titulo'),
        ),
    ]
