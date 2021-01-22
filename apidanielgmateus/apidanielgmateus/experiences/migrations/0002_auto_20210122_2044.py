# Generated by Django 3.0.4 on 2021-01-22 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(verbose_name='Descricao:'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='ended_at',
            field=models.DateTimeField(verbose_name='Saída em:'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='started_at',
            field=models.DateTimeField(verbose_name='Entrada em:'),
        ),
    ]
