# Generated by Django 3.1.2 on 2020-10-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumnos', '0002_auto_20201006_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='padre',
            name='dni',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='DNI'),
        ),
    ]
