"""PinochoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Apps.Alumnos.views import Home, ListadoAlumnos, ListadoPadres, NuevoAlumno, NuevoPadre, AlumnoEdit, AlumnoDelete, PadreEdit, PadreDelete
from Apps.Adeudos.views import NuevoAdeudo, ListadoAdeudos, AdeudoEdit, AdeudoDelete
from Apps.Contabilidad.views import ListadoIngresos, NuevoIngreso, IngresoDelete, IngresoEdit, ListadoGastos, \
                                    NuevoGasto, GastoDelete, GastoEdit, CategoriasIngresos, CategoriasGastos, \
                                    NuevaCatIngreso, NuevaCatGastos, Portada_contabilidad, Portada_contabilidad_plus, \
                                    Portada_contabilidad_plus2, CatGastoDelete, CatGastoEdit, CatIngresoEdit, CatIngresoDelete, \
                                    ReciboPDF, NuevoRecibo, EditarRecibo, ListadoRecibos, ReciboDelete   
                                       
from Apps.Login.views import Login, LogoutUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(Home.as_view()), name = 'Home'),
    path('accounts/login/', Login.as_view(), name = 'Login'),
    path('logout/', LogoutUser, name = 'Logout'),
    path('Alumnos/', login_required(ListadoAlumnos.as_view()), name = 'Alumnos'),
    path('Padres/', login_required(ListadoPadres.as_view()), name = 'Padres'),
    path('NuevoAlumno/', login_required(NuevoAlumno.as_view()), name = 'NuevoAlumno'),
    path('NuevoPadre/', login_required(NuevoPadre.as_view()), name = 'NuevoPadre'),
    path('AlumnoEdit/<int:pk>/', login_required(AlumnoEdit.as_view()), name = 'AlumnoEdit'),
    path('AlumnoDelete/<int:pk>/', login_required(AlumnoDelete.as_view()), name = 'AlumnoDelete'),
    path('PadreEdit/<int:pk>/', login_required(PadreEdit.as_view()), name = 'PadreEdit'),
    path('PadreDelete/<int:pk>/', login_required(PadreDelete.as_view()), name = 'PadreDelete'),
    #ADEUDOS
    path('Adeudos/', login_required(ListadoAdeudos.as_view()), name = 'Adeudos'),
    path('NuevoAdeudo/', login_required(NuevoAdeudo.as_view()), name = 'NuevoAdeudo'),
    path('AdeudoEdit/<int:pk>/', login_required(AdeudoEdit.as_view()), name = 'AdeudoEdit'),
    path('AdeudoDelete/<int:pk>/', login_required(AdeudoDelete.as_view()), name = 'AdeudoDelete'),
    #CONTABILIDAD
    path('Portada_contabilidad/', login_required(Portada_contabilidad.as_view()), name = 'Portada_contabilidad'),
    path('Portada_contabilidad_plus/', login_required(Portada_contabilidad_plus.as_view()), name = 'Portada_contabilidad_plus'),
    path('Portada_contabilidad_plus2/', login_required(Portada_contabilidad_plus2.as_view()), name = 'Portada_contabilidad_plus2'),
    path('Ingresos/', login_required(ListadoIngresos.as_view()), name = 'Ingresos'),
    path('NuevoIngreso/', login_required(NuevoIngreso.as_view()), name = 'NuevoIngreso'),
    path('IngresoEdit/<int:pk>/', login_required(IngresoEdit.as_view()), name = 'IngresoEdit'),
    path('IngresoDelete/<int:pk>/', login_required(IngresoDelete.as_view()), name = 'IngresoDelete'),
    path('Gastos/', login_required(ListadoGastos.as_view()), name = 'Gastos'),
    path('NuevoGasto/', login_required(NuevoGasto.as_view()), name = 'NuevoGasto'),
    path('GastoEdit/<int:pk>/', login_required(GastoEdit.as_view()), name = 'GastoEdit'),
    path('GastoDelete/<int:pk>/', login_required(GastoDelete.as_view()), name = 'GastoDelete'),
    path('Categorias_Ingresos/', login_required(CategoriasIngresos.as_view()), name = 'CategoriasIngresos'),
    path('Nueva_Cat_Gasto/', login_required(NuevaCatGastos.as_view()), name = 'NuevaCatGastos'),
    path('Categorias_Gastos/', login_required(CategoriasGastos.as_view()), name = 'CategoriasGastos'),
    path('Nueva_Cat_Ingresos/', login_required(NuevaCatIngreso.as_view()), name = 'NuevaCatIngresos'),
    path('Cat_Gastos_Delete/<int:pk>/', login_required(CatGastoDelete.as_view()), name = 'CatGastoDelete'),
    path('Cat_Gastos_Edit/<int:pk>/', login_required(CatGastoEdit.as_view()), name = 'CatGastoEdit'),
    path('Cat_Ingresos_Delete/<int:pk>/', login_required(CatIngresoDelete.as_view()), name = 'CatIngresoDelete'),
    path('Cat_Ingresos_Edit/<int:pk>/', login_required(CatIngresoEdit.as_view()), name = 'CatIngresoEdit'),
    #RECIBOS
    path('NuevoRecibo/', login_required(NuevoRecibo.as_view()), name = 'NuevoRecibo'),
    path('ListadoRecibos/', login_required(ListadoRecibos.as_view()), name = 'Recibos'),
    path('EditRecibo/<int:pk>/', login_required(EditarRecibo.as_view()), name = 'ReciboEdit'),
    path('BorrarRecibo/<int:pk>/', login_required(ReciboDelete.as_view()), name = 'ReciboDelete'),
    path('ReciboPDF/<int:pk>/', login_required(ReciboPDF.as_view()), name = 'ReciboPDF'),
] + static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    