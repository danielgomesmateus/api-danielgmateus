# Generated by Django 3.0.4 on 2021-01-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_formations', '0002_auto_20210124_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicformation',
            name='ended_at',
            field=models.DateField(blank=True, null=True, verbose_name='Saída em:'),
        ),
        migrations.AlterField(
            model_name='academicformation',
            name='started_at',
            field=models.DateField(verbose_name='Entrada em:'),
        ),
    ]
