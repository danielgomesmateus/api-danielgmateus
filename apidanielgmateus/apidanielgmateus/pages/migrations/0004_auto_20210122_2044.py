# Generated by Django 3.0.4 on 2021-01-22 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200418_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(verbose_name='Conteúdo:'),
        ),
    ]