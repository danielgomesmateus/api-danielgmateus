# Generated by Django 3.0.4 on 2020-03-14 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200314_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['id', 'name', 'categorie', 'description_short', 'content', 'created_at', 'updated_at'], 'verbose_name': 'Projeto', 'verbose_name_plural': 'Projetos'},
        ),
        migrations.AlterField(
            model_name='project',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='projects.Categorie'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ImageField(upload_to='projects', verbose_name='Imagem de capa:'),
        ),
    ]
