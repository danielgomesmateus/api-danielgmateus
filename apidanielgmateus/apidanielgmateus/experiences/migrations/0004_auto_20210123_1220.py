# Generated by Django 3.0.4 on 2021-01-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0003_auto_20210123_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(verbose_name='Descrição:'),
        ),
    ]
