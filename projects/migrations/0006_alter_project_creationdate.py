# Generated by Django 4.2.2 on 2023-06-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_creationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creationDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
