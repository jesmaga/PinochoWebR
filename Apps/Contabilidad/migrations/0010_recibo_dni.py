# Generated by Django 3.1.2 on 2020-11-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contabilidad', '0009_auto_20201110_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibo',
            name='dni',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]