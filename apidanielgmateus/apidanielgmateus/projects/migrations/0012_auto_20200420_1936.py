# Generated by Django 3.0.4 on 2020-04-20 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='files',
            field=models.FileField(max_length=255, upload_to='projects/images', verbose_name='Arquivos do projeto:'),
        ),
    ]
