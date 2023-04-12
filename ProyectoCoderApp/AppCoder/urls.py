from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('agrega-avion/<marca>/<matricula>', avion),
    path('lista-avion/', lista_avion),
    path('', inicio, name="Inicio"),
    path('avion/', avion, name="Avion"),
    path('piloto/', piloto, name="Piloto"),
    path('pasajero/', pasajero, name="Pasajero"),
    path('planDeVuelo/', planDeVuelo, name="PlanDeVuelo"),
    path('avionFormulario/', avionFormulario, name="AvionFormulario"),
    path('busquedaMatricula/', busquedaMatricula, name="BusquedaMatricula"),
    path('buscar/', buscar),
]