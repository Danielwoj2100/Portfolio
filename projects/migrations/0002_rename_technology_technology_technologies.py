# Generated by Django 4.2.2 on 2023-06-30 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technology',
            old_name='technology',
            new_name='technologies',
        ),
    ]