from django.db import models

# Create your models here.

class Curso(models.Model):

    Curso = models.CharField(max_length=5)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:

        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):

        return self.Curso    

class Clase(models.Model):

    clase=models.CharField(max_length=10)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name='Clase'
        verbose_name_plural='Clases'

    def __str__(self):

        return self.clase

class Padre(models.Model):

    Id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=25)
    Apellidos=models.CharField(max_length=50)
    NumeroCuenta = models.CharField(verbose_name='Numero de Cuenta', max_length=24)
    dni = models.CharField(max_length=9, null=True, blank=True, verbose_name='DNI')
    Telefono1= models.CharField(verbose_name='Tlf 1',max_length=12, blank=True, null=True)
    Telefono2= models.CharField(verbose_name='Tlf 2',max_length=12, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name='Padre'
        verbose_name_plural='Padres'   

    def __str__(self):

        return '%s %s' % (self.Nombre, self.Apellidos)  

class Alumno(models.Model):

    Id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=25)
    Apellidos=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='Alumnos', null=True, blank=True)
    Clase=models.ForeignKey(Clase, null=True, blank=True, on_delete=models.CASCADE)
    Curso=models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    Padre=models.ForeignKey(Padre, null=True, blank=True, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name='Alumno'
        verbose_name_plural='Alumnos'

    def __str__(self):

        return '%s %s' % (self.Nombre, self.Apellidos)

   