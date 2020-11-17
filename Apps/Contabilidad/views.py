from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, TemplateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from .models import Ingreso, Gasto, Cat_Gasto, Cat_Ingreso, year, Recibo
from Apps.Alumnos.models import Padre
from Apps.Alumnos.forms import PadreForm
from .forms import CatGastoForm, CatIngresoForm, IngresoForm, GastoForm, YearForm, ReciboForm
from datetime import datetime

import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.

class Portada_contabilidad(TemplateView):

    template_name = 'portada_contabilidad.html' 
    
    @classmethod
    def ano(cls):

        data1 = datetime.now().year
        data2 = data1 + 1
        data = str(str(data1)+'/'+str(data2))
        return data

    # CALCULOS PARA INGRESOS

    @classmethod
    def get_total_ingresos(cls):
        data = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.all()])
        return data


    @classmethod
    def get_ingresos_mes(cls):
        total = dict()
        total_plus = dict()
        ano = datetime.now().year
        anoplus = ano + 1
        for i in range(1, 13):
            total_mes = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.filter(fecha__month= i, fecha__year= ano)])
            total [i] = total_mes
            valores = list(total.values())
            valores_final = valores[8:13]
        for i in range(1, 13):
            total_mes_plus = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.filter(fecha__month= i, fecha__year= anoplus)])
            total_plus [i] = total_mes_plus
            valores_plus = list(total_plus.values())
            valores_final_plus = valores_plus[0:8]

        valores_final.extend(valores_final_plus)
        ingresos_total_ano = sum(valores_final)
        valores_final.append(ingresos_total_ano)
        return valores_final

    @classmethod
    def get_total_ingresos_curso(cls):
        ingresos = cls.get_ingresos_mes()
        total = sum(ingresos)
        return total    

    @classmethod
    def get_total_ingresos_ano(cls):
        ano = datetime.today().year
        total = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.filter(fecha__year= ano)])
        return total      

    # CALCULOS PARA GASTOS

    @classmethod
    def get_total_gastos(cls):
        data = sum([Gasto.cantidad for Gasto in Gasto.objects.all()])
        return data

    @classmethod
    def get_gastos_mes(cls):

        total = dict()
        total_plus = dict()
        ano = datetime.today().year
        anoplus = ano + 1
        for i in range(1, 13):
            total_mes = sum([Gasto.cantidad for Gasto in Gasto.objects.filter(fecha__month= i, fecha__year= ano)])
            total [i] = total_mes
            valores = list(total.values())
            valores_final = valores[8:13]
        for i in range(1, 13):
            total_mes_plus = sum([Gasto.cantidad for Gasto in Gasto.objects.filter(fecha__month= i, fecha__year= anoplus)])
            total_plus [i] = total_mes_plus
            valores_plus = list(total_plus.values())
            valores_final_plus = valores_plus[0:8]

        valores_final.extend(valores_final_plus)
        gastos_total_ano = sum(valores_final)
        valores_final.append(gastos_total_ano)
        return valores_final

    @classmethod
    def get_total_gastos_curso(cls):
        gastos = cls.get_gastos_mes()
        total = sum(gastos)
        return total
        
    #    total = sum([Gasto.cantidad for Gasto in Gasto.objects.filter(fecha__year= ano)])
    #    return gastos  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['title'] = 'Gráfica barras'
        context['grafico_ingresos'] = self.get_ingresos_mes()
        context['grafico_gastos'] = self.get_gastos_mes()
        context['total_ingresos_curso'] = self.get_total_ingresos_curso()
        context['total_gastos_curso'] = self.get_total_gastos_curso()
        context['ano'] = self.ano()
        return context

class Portada_contabilidad_plus(TemplateView):

    template_name = 'portada_contabilidad_plus.html' 
    
    @classmethod
    def ano(cls):

        data1 = datetime.now().year - 1
        data2 = data1 + 1
        data = str(str(data1)+'/'+str(data2))
        return data

    # CALCULOS PARA INGRESOS

    @classmethod
    def get_total_ingresos(cls):
        data = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.all()])
        return data

    @classmethod
    def get_ingresos_mes(cls):
        total = dict()
        total_plus = dict()
        ano = datetime.now().year - 1
        anoplus = ano + 1
        for i in range(1, 13):
            total_mes = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.filter(fecha__month= i, fecha__year= ano)])
            total [i] = total_mes
            valores = list(total.values())
            valores_final = valores[8:13]
        for i in range(1, 13):
            total_mes_plus = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.filter(fecha__month= i, fecha__year= anoplus)])
            total_plus [i] = total_mes_plus
            valores_plus = list(total_plus.values())
            valores_final_plus = valores_plus[0:8]

        valores_final.extend(valores_final_plus)
        ingresos_total_ano = sum(valores_final)
        valores_final.append(ingresos_total_ano)
        return valores_final

    @classmethod
    def get_total_ingresos_curso(cls):
        ingresos = cls.get_ingresos_mes()
        total = sum(ingresos)
        return total    

    @classmethod
    def get_total_ingresos_ano(cls):
        ano = datetime.today().year - 1
        total = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.filter(fecha__year= ano)])
        return total      

    # CALCULOS PARA GASTOS

    @classmethod
    def get_total_gastos(cls):
        data = sum([Gasto.cantidad for Gasto in Gasto.objects.all()])
        return data

    @classmethod
    def get_gastos_mes(cls):

        total = dict()
        total_plus = dict()
        ano = datetime.today().year - 1
        anoplus = ano + 1
        for i in range(1, 13):
            total_mes = sum([Gasto.cantidad for Gasto in Gasto.objects.filter(fecha__month= i, fecha__year= ano)])
            total [i] = total_mes
            valores = list(total.values())
            valores_final = valores[8:13]
        for i in range(1, 13):
            total_mes_plus = sum([Gasto.cantidad for Gasto in Gasto.objects.filter(fecha__month= i, fecha__year= anoplus)])
            total_plus [i] = total_mes_plus
            valores_plus = list(total_plus.values())
            valores_final_plus = valores_plus[0:8]

        valores_final.extend(valores_final_plus)
        gastos_total_ano = sum(valores_final)
        valores_final.append(gastos_total_ano)
        return valores_final

    @classmethod
    def get_total_gastos_curso(cls):
        gastos = cls.get_gastos_mes()
        total = sum(gastos)
        return total
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['title'] = 'Gráfica barras'
        context['grafico_ingresos'] = self.get_ingresos_mes()
        context['grafico_gastos'] = self.get_gastos_mes()
        context['total_ingresos_curso'] = self.get_total_ingresos_curso()
        context['total_gastos_curso'] = self.get_total_gastos_curso()
        context['ano'] = self.ano()
        return context

class Portada_contabilidad_plus2(TemplateView):

    template_name = 'portada_contabilidad_plus2.html' 
    
    @classmethod
    def ano(cls):

        data1 = datetime.now().year - 2
        data2 = data1 + 1
        data = str(str(data1)+'/'+str(data2))
        return data

    # CALCULOS PARA INGRESOS

    @classmethod
    def get_total_ingresos(cls):
        data = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.all()])
        return data

    @classmethod
    def get_ingresos_mes(cls):
        total = dict()
        total_plus = dict()
        ano = datetime.now().year - 2
        anoplus = ano + 1
        for i in range(1, 13):
            total_mes = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.filter(fecha__month= i, fecha__year= ano)])
            total [i] = total_mes
            valores = list(total.values())
            valores_final = valores[8:13]
        for i in range(1, 13):
            total_mes_plus = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.filter(fecha__month= i, fecha__year= anoplus)])
            total_plus [i] = total_mes_plus
            valores_plus = list(total_plus.values())
            valores_final_plus = valores_plus[0:8]

        valores_final.extend(valores_final_plus)
        ingresos_total_ano = sum(valores_final)
        valores_final.append(ingresos_total_ano)
        return valores_final

    @classmethod
    def get_total_ingresos_curso(cls):
        ingresos = cls.get_ingresos_mes()
        total = sum(ingresos)
        return total    

    @classmethod
    def get_total_ingresos_ano(cls):
        ano = datetime.today().year - 2
        total = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.filter(fecha__year= ano)])
        return total      

    # CALCULOS PARA GASTOS

    @classmethod
    def get_total_gastos(cls):
        data = sum([Gasto.cantidad for Gasto in Gasto.objects.all()])
        return data

    @classmethod
    def get_gastos_mes(cls):

        total = dict()
        total_plus = dict()
        ano = datetime.today().year - 2
        anoplus = ano + 1
        for i in range(1, 13):
            total_mes = sum([Gasto.cantidad for Gasto in Gasto.objects.filter(fecha__month= i, fecha__year= ano)])
            total [i] = total_mes
            valores = list(total.values())
            valores_final = valores[8:13]
        for i in range(1, 13):
            total_mes_plus = sum([Gasto.cantidad for Gasto in Gasto.objects.filter(fecha__month= i, fecha__year= anoplus)])
            total_plus [i] = total_mes_plus
            valores_plus = list(total_plus.values())
            valores_final_plus = valores_plus[0:8]

        valores_final.extend(valores_final_plus)
        gastos_total_ano = sum(valores_final)
        valores_final.append(gastos_total_ano)
        return valores_final

    @classmethod
    def get_total_gastos_curso(cls):
        gastos = cls.get_gastos_mes()
        total = sum(gastos)
        return total
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['title'] = 'Gráfica barras'
        context['grafico_ingresos'] = self.get_ingresos_mes()
        context['grafico_gastos'] = self.get_gastos_mes()
        context['total_ingresos_curso'] = self.get_total_ingresos_curso()
        context['total_gastos_curso'] = self.get_total_gastos_curso()
        context['ano'] = self.ano()
        return context

class NuevoIngreso(CreateView):

    model = Ingreso
    form_class = IngresoForm      
    template_name = 'NuevoIngreso.html'  
    success_url = reverse_lazy('Ingresos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['title'] = 'Nuevo Ingreso'
        context['cancel']= reverse_lazy('Ingresos')
        context['submit'] = 'Añadir'
        return context

class ListadoIngresos(ListView):

    model = Ingreso
    form_class = IngresoForm     
    template_name = 'ListadoIngresos.html'  
    success_url = reverse_lazy('Ingresos')
        
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Ingresos'
        context['submit'] = reverse_lazy('NuevoIngreso')
        return context           

class IngresoEdit(UpdateView):

    model = Ingreso
    form_class = IngresoForm
    template_name = 'NuevoIngreso.html'   
    success_url = reverse_lazy('Ingresos') 

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Ingreso'
        context['cancel']= reverse_lazy('Ingresos')
        context['submit'] = 'Actualizar'
        return context    

class IngresoDelete(DeleteView):

    model = Ingreso
    template_name = 'IngresoDelete.html'  
    success_url = reverse_lazy('Ingresos')  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Ingreso'
        context['cancel']= reverse_lazy('Ingresos')
        return context     

class NuevoGasto(CreateView):

    model = Gasto
    form_class = GastoForm      
    template_name = 'NuevoGasto.html'  
    success_url = reverse_lazy('Gastos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['title'] = 'Nuevo Gasto'
        context['cancel']= reverse_lazy('Gastos')
        context['submit'] = 'Añadir'
        return context

class ListadoGastos(ListView):

    model = Gasto
    form_class = GastoForm     
    template_name = 'ListadoGastos.html'  
    success_url = reverse_lazy('Gastos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Gastos'
        context['submit'] = reverse_lazy('NuevoGasto')
        return context                 

class GastoEdit(UpdateView):

    model = Gasto
    form_class = GastoForm
    template_name = 'NuevoGasto.html'   
    success_url = reverse_lazy('Gastos') 

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Gasto'
        context['cancel']= reverse_lazy('Gastos')
        context['submit'] = 'Actualizar'
        return context    

class GastoDelete(DeleteView):

    model = Gasto
    template_name = 'GastoDelete.html'  
    success_url = reverse_lazy('Gastos')  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Gasto'
        context['cancel']= reverse_lazy('Gastos')
        return context    

class NuevaCatIngreso(CreateView):

    model = Cat_Ingreso
    form_class = CatIngresoForm      
    template_name = 'NuevaCatIngreso.html'  
    success_url = reverse_lazy('CategoriasIngresos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['title'] = 'Nueva Categoría Ingresos'
        context['cancel']= reverse_lazy('CategoriasIngresos')
        context['submit'] = 'Añadir'
        return context

class CategoriasIngresos(ListView):

    model = Cat_Ingreso
    form_class = CatIngresoForm     
    template_name = 'CategoriasIngresos.html'  
    success_url = reverse_lazy('CategoriasIngresos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Categorias Ingresos'
        context['submit'] = reverse_lazy('NuevaCatIngresos')
        return context          

class NuevaCatGastos(CreateView):

    model = Cat_Gasto
    form_class = CatGastoForm      
    template_name = 'NuevaCatGasto.html'  
    success_url = reverse_lazy('CategoriasGastos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['title'] = 'Nueva Categoría Gastos'
        context['cancel']= reverse_lazy('CategoriasGastos')
        context['submit'] = 'Añadir'
        return context

class CategoriasGastos(ListView):

    model = Cat_Gasto
    form_class = CatGastoForm     
    template_name = 'CategoriasGastos.html'  
    success_url = reverse_lazy('CategoriasGastos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Categorias Gastos'
        context['submit'] = reverse_lazy('NuevaCatGastos')
        return context   

class CatGastoDelete(DeleteView):

    model = Cat_Gasto
    template_name = 'CatGastoDelete.html'  
    success_url = reverse_lazy('CategoriasGastos')  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Categoría'
        context['cancel']= reverse_lazy('CategoriasGastos')
        return context   

class CatGastoEdit(UpdateView):

    model = Cat_Gasto
    form_class = CatGastoForm
    template_name = 'CatGastoEdit.html'   
    success_url = reverse_lazy('CategoriasGastos') 

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Categoría'
        context['cancel']= reverse_lazy('CategoriasGastos')
        context['submit'] = 'Actualizar'
        return context         

class CatIngresoDelete(PermissionRequiredMixin, DeleteView):

    model = Cat_Ingreso
    template_name = 'CatIngresoDelete.html'  
    success_url = reverse_lazy('CategoriasIngresos')  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Categoría'
        context['cancel']= reverse_lazy('CategoriasIngresos')
        return context   

class CatIngresoEdit(PermissionRequiredMixin, UpdateView):

    model = Cat_Ingreso
    form_class = CatIngresoForm
    template_name = 'CatIngresoEdit.html'   
    success_url = reverse_lazy('CategoriasIngresos') 

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Categoría'
        context['cancel']= reverse_lazy('CategoriasIngresos')
        context['submit'] = 'Actualizar'
        return context   

class NuevoRecibo(CreateView):

    model = Recibo
    form_class = ReciboForm      
    template_name = 'NuevoRecibo.html'  
    success_url = reverse_lazy('Recibos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['title'] = 'Nuevo Recibo'
        context['cancel']= reverse_lazy('Recibos')
        context['submit'] = 'Añadir'
        return context

class ListadoRecibos(ListView):

    model = Recibo
    form_class = ReciboForm   
    template_name = 'ListadoRecibos.html'  
    success_url = reverse_lazy('Recibos')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Recibos'
        context['submit'] = reverse_lazy('NuevoRecibo')
        return context                 

class EditarRecibo(UpdateView):

    model = Recibo
    form_class = ReciboForm      
    template_name = 'NuevoRecibo.html'  
    success_url = reverse_lazy('ListadoRecibos')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['title'] = 'Editar Recibo'
        context['cancel']= reverse_lazy('Recibos')
        context['submit'] = 'Modificar'
        return context   

class ReciboDelete(DeleteView):

    model = Recibo
    template_name = 'ReciboDelete.html'  
    success_url = reverse_lazy('Recibos')  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Recibo'
        context['cancel']= reverse_lazy('Recibos')
        return context                


class ReciboPDF(View):

    def get(self, request, *args, **kwargs):

        try:
            template = get_template('ReciboPDF.html')
            context = {
                'Recibo': Recibo.objects.get(pk=self.kwargs['pk']),
                'comp': {'name': 'C.E.I. Pinocho', 'ruc': 'www.ceipinocho.es', 'nif': 'N.I.F.: 27.905.670-T', 'address': 'C/ Alvar Nuñez, locales 6, 7 y 8'},
                'icon': '{}{}'.format(settings.MEDIA_ROOT, '/logotipo_pinocho.jpg')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #incluir la linea de abajo para guardar directamente
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # create a pdf
            pisa.CreatePDF(html, dest=response)
            return response    
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('Recibos'))    

        