# Generated by Django 3.0.4 on 2020-04-20 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20200420_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='files',
            field=models.FileField(max_length=255, upload_to='projects/files', verbose_name='Arquivos do projeto:'),
        ),
    ]
