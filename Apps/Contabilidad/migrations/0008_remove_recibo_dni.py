# Generated by Django 3.1.2 on 2020-11-10 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contabilidad', '0007_auto_20201110_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recibo',
            name='dni',
        ),
    ]
