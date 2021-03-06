# Generated by Django 3.1.2 on 2020-11-08 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contabilidad', '0004_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=9)),
                ('concepto', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('cantidad', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Recibo',
                'verbose_name_plural': 'Recibos',
            },
        ),
    ]
