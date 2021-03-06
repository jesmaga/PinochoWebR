# Generated by Django 3.1.2 on 2020-10-25 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat_Gasto',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria Gasto',
                'verbose_name_plural': 'Categorias Gastos',
            },
        ),
        migrations.CreateModel(
            name='Cat_Ingreso',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria Ingreso',
                'verbose_name_plural': 'Categorias Ingreso',
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('concepto', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Contabilidad.cat_ingreso')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
            },
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('concepto', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Contabilidad.cat_gasto')),
            ],
            options={
                'verbose_name': 'Gasto',
                'verbose_name_plural': 'Gastos',
            },
        ),
    ]
