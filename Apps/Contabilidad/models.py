from django.db import models
from datetime import datetime
from PinochoWeb import settings
from Apps.Alumnos.models import Padre

# Create your models here.

class year(models.Model):
    
    actual_year = datetime.now().year
    ano = models.CharField(max_length=4, default=actual_year)

    def __str__(self):

        return  '%s' % self.ano 

class Cat_Ingreso(models.Model):

    Id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name='Categoria Ingreso'
        verbose_name_plural='Categorias Ingreso'   

    def __str__(self):

        return  '%s' % self.categoria 

class Cat_Gasto(models.Model):

    Id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name='Categoria Gasto'
        verbose_name_plural='Categorias Gastos'   

    def __str__(self):

        return  '%s' % self.categoria         

class Ingreso(models.Model):

    Id = models.AutoField(primary_key=True)
    concepto = models.CharField(max_length=30)
    categoria = models.ForeignKey(Cat_Ingreso, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.FloatField(default=0.00)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)  

    class Meta:

        verbose_name='Ingreso'
        verbose_name_plural='Ingresos'   

    def __str__(self):

        return  '%s %s' % (self.concepto, self.cantidad)


class Gasto(models.Model):

    Id = models.AutoField(primary_key=True)
    concepto = models.CharField(max_length=30)
    categoria = models.ForeignKey(Cat_Gasto, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.FloatField(default=0.00)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)  

    class Meta:

        verbose_name='Gasto'
        verbose_name_plural='Gastos'   

    def __str__(self):

        return  '%s %s' % (self.concepto, self.cantidad)  

class Recibo(models.Model):

    Id = models.AutoField(primary_key=True)
#    nombre = models.CharField(max_length=30, blank=True, null=True)
#    apellidos = models.CharField(max_length=50, blank=True, null=True)
#    dni = models.CharField(max_length=9, blank=True, null=True)
    padre = models.ForeignKey(Padre, null=True, blank=True, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=30)
    fecha = models.DateField()
    cantidad = models.FloatField(default=0.00)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)  

    class Meta:

        verbose_name='Recibo'
        verbose_name_plural='Recibos'   

    def __str__(self):

        return  '%s %s' % (self.concepto, self.cantidad)  

