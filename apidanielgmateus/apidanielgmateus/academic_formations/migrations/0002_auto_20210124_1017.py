# Generated by Django 3.0.4 on 2021-01-24 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic_formations', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AcademicFormations',
            new_name='AcademicFormation',
        ),
    ]