from django.db import models
from Apps.Alumnos.models import Padre
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your models here.


class Mes(models.Model):

    mes = models.CharField(max_length=15)
    año = models.IntegerField()

    class Meta:

        verbose_name='Mes'
        verbose_name_plural='Meses'   

    def __str__(self):

        return '%s %s' % (self.mes, self.año)  

class Concepto(models.Model):

    Concepto = models.CharField(max_length=25)  

    class Meta:

        verbose_name='Concepto'
        verbose_name_plural='Conceptos'   

    def __str__(self):

        return '%s' % self.Concepto 

class Adeudo(models.Model):

    
    Importe = models.DecimalField(default=0, max_digits = 5, decimal_places = 2)
    Concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    Mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    Padre = models.ForeignKey(Padre, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:

        verbose_name='Adeudo'
        verbose_name_plural='Adeudos'   

    def __str__(self):

        return '%s' % self.Importe