# Generated by Django 3.1.2 on 2020-11-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adeudos', '0004_auto_20201031_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mes',
            name='mes',
            field=models.CharField(max_length=15),
        ),
    ]
