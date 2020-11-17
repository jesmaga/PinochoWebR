from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy
from .models import Mes, Concepto, Adeudo
from Apps.Alumnos.models import Alumno
from .forms import ConceptoForm, AdeudoForm
from Apps.Alumnos.forms import AlumnoForm

# Create your views here.


class NuevoAdeudo(CreateView):

    model = Adeudo
    form_class = AdeudoForm      
    template_name = 'Nuevoadeudo.html'  
    success_url = reverse_lazy('Adeudos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['title'] = 'Nuevo Adeudo'
        context['cancel']= reverse_lazy('Adeudos')
        context['submit'] = 'Añadir'
        return context

    #def post(self, request, *args, **kwargs):
    #    self.object = self.get_object
    #    form = self.form_class(request.POST)
    #    if form.is_valid():
    #        solicitud = form.save(commit=False)
    #        solicitud.save()
    #        return HttpResponseRedirect(self.get_success_url())
    #    else:
    #        return self.render_to_response(self.get_context_data(form = form))    

class ListadoAdeudos(ListView):

    model = Adeudo
    second_model = Alumno
    form_class = AdeudoForm   
    second_form_class = AlumnoForm   
    template_name = 'Listadoadeudos.html'  
    success_url = reverse_lazy('Adeudos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Adeudos'
        context['submit'] = reverse_lazy('NuevoAdeudo')
        return context   

class AdeudoEdit(UpdateView):

    model = Adeudo
    form_class = AdeudoForm
    template_name = 'NuevoAdeudo.html'   
    success_url = reverse_lazy('Adeudos') 

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Adeudo'
        context['cancel']= reverse_lazy('Adeudos')
        context['submit'] = 'Actualizar'
        return context    

class AdeudoDelete(DeleteView):

    model = Adeudo
    template_name = 'AdeudoDelete.html'  
    success_url = reverse_lazy('Adeudos')  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Adeudo'
        context['cancel']= reverse_lazy('Adeudos')
        return context     

