from django import forms
from .models import Alumno, Padre
from django.forms import ModelForm

class AlumnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Alumno
        fields = '__all__'

        widgets = {
                'Nombre': forms.TextInput(attrs={
                    'placeholder': 'Nombre del Alumno ...',
                    'class': 'form-control', }),
                'Apellidos': forms.TextInput(attrs={
                    'placeholder': 'Apellidos del Alumno ...',
                    'class': 'form-control', }),
                'Clase': forms.Select(attrs={
                    'class': 'form-control', }),  
                'Curso': forms.Select(attrs={
                    'class': 'form-control', }), 
                'Padre': forms.Select(attrs={
                    'class': 'form-control', }),              
            }    

    

class PadreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Padre
        fields = '__all__'        
            

        widgets = {
                'Nombre': forms.TextInput(attrs={
                    'placeholder': 'Nombre del Padre/Madre ...',
                    'class': 'form-control', }),
                'Apellidos': forms.TextInput(attrs={
                    'placeholder': 'Apellidos del Padre/Madre ...',
                    'class': 'form-control', }),  
                'NumeroCuenta': forms.TextInput(attrs={
                    'placeholder': 'IBAN ...',
                    'class': 'form-control', }), 
                'Telefono1': forms.TextInput(attrs={
                    'placeholder': 'Teléfono fijo ...',
                    'class': 'form-control', }),  
                'dni': forms.TextInput(attrs={
                    'placeholder': 'Introduzca el D.N.I. ...',
                    'class': 'form-control', }),     
                'Telefono2': forms.TextInput(attrs={
                    'placeholder': 'Teléfono móvil ...',
                    'class': 'form-control', }),           
            }       

