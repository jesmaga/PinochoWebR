# Generated by Django 3.1.2 on 2020-10-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adeudos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adeudo',
            name='Importe',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
