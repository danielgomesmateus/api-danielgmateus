# Generated by Django 3.0.4 on 2021-01-22 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210121_2259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categorie',
            new_name='category',
        ),
    ]