from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect,HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy
from .models import Curso, Clase, Alumno, Padre
from Apps.Contabilidad.models import Ingreso, Gasto
from .forms import AlumnoForm, PadreForm
from datetime import datetime


# Create your views here.

class Home(TemplateView):

    template_name = 'home.html'

    @classmethod
    def ano(request):
        data = datetime.today().year
        curso = str('20/21')
        return curso

    @classmethod
    def get_total_ingresos(cls):
        data = sum([Ingreso.cantidad for Ingreso in Ingreso.objects.all()])
        return data

    @classmethod
    def get_ingresos_mes(cls):
        total = dict()
        total_plus = dict()
        ano = datetime.today().year
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
        return valores_final

    @classmethod
    def get_total_ingresos_curso(cls):
        ingresos = cls.get_ingresos_mes()
        total = sum(ingresos)
        return total     

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
        return valores_final    

    @classmethod
    def get_total_gastos_curso(cls):
        gastos = cls.get_gastos_mes()
        total = sum(gastos)
        return total   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['grafico_ingresos'] = self.get_ingresos_mes()
        context['grafico_gastos'] = self.get_gastos_mes()
        context['total_ingresos_curso'] = self.get_total_ingresos_curso()
        context['total_gastos_curso'] = self.get_total_gastos_curso()
        context['ano'] = self.ano()
        return context

class ListadoAlumnos(ListView):

    model = Alumno
    template_name = 'Alumnos.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Alumnos'
        context['submit']= reverse_lazy('NuevoAlumno')
        return context

class ListadoPadres(ListView):

    model = Padre
    template_name = 'Padres.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Padres'
        context['submit']= reverse_lazy('NuevoPadre')
        return context        
    
class NuevoAlumno(CreateView):

    model = Alumno
    form_class = AlumnoForm
    template_name = 'NuevoAlumno.html'   
    success_url = reverse_lazy('Alumnos') 

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Alumno'
        context['cancel']= reverse_lazy('Alumnos')
        context['submit'] = 'Añadir'
        return context

class NuevoPadre(CreateView):

    model = Padre
    form_class = PadreForm
    template_name = 'NuevoPadre.html'   
    success_url = reverse_lazy('Padres') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Padre/Madre'
        context['cancel']= reverse_lazy('Padres')
        context['submit'] = 'Añadir'
        
        return context

class AlumnoEdit(UpdateView):

    model = Alumno
    form_class = AlumnoForm
    template_name = 'NuevoAlumno.html'   
    success_url = reverse_lazy('Alumnos') 

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Alumno'
        context['cancel']= reverse_lazy('Alumnos')
        context['submit'] = 'Actualizar'
        return context    

class AlumnoDelete(DeleteView):

    model = Alumno
    template_name = 'AlumnoDelete.html'  
    success_url = reverse_lazy('Alumnos')  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Alumno'
        context['cancel']= reverse_lazy('Alumnos')
        return context    

class PadreEdit(UpdateView):

    model = Padre
    form_class = PadreForm
    template_name = 'NuevoPadre.html'   
    success_url = reverse_lazy('Padres') 

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Padre'
        context['cancel']= reverse_lazy('Padres')
        context['submit'] = 'Actualizar'
        return context    

class PadreDelete(DeleteView):

    model = Padre
    template_name = 'PadreDelete.html'  
    success_url = reverse_lazy('Padres')  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Padre'
        context['cancel']= reverse_lazy('Padres')
        return context          
    
