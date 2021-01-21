# Generated by Django 3.0.4 on 2020-03-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nome:')),
                ('description_short', models.CharField(max_length=50, verbose_name='Descrição curta:')),
                ('content', models.TextField(verbose_name='Conteúdo:')),
                ('cover_image', models.ImageField(upload_to='images', verbose_name='Imagem de capa:')),
                ('slug', models.SlugField(verbose_name='Identificador:')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
                'ordering': ['id', 'name', 'description_short', 'content', 'created_at', 'updated_at'],
            },
        ),
    ]
