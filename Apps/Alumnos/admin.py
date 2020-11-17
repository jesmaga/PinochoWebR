from django.contrib import admin
from .models import Curso, Clase, Alumno, Padre

# Register your models here.

admin.site.register(Curso)
admin.site.register(Clase)
admin.site.register(Alumno)
admin.site.register(Padre)