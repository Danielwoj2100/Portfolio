# Generated by Django 4.2.2 on 2023-07-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='technology',
            name='technologies',
            field=models.CharField(max_length=25),
        ),
    ]
