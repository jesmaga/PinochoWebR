from django.contrib import admin
from .models import Cat_Gasto, Cat_Ingreso, Gasto, Ingreso, year, Recibo

# Register your models here.

admin.site.register(Cat_Ingreso)
admin.site.register(Cat_Gasto)
admin.site.register(Gasto)
admin.site.register(Ingreso)
admin.site.register(year)
admin.site.register(Recibo)