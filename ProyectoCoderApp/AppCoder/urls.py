from django.contrib import admin
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

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
    path('buscar/', buscar, name="Buscar"),
    path('listaPilotos/', listaPilotos, name="ListaPilotos"),
    path('crea-piloto/', crea_piloto, name="CreaPiloto"),
    path('elimina-piloto/<int:id>', eliminarPiloto, name="EliminaPiloto"),
    path('editar-piloto/<int:id>', editar_piloto, name="EditarPiloto"),
    path('listaAvion/', AvionList.as_view(), name="ListaAvion"),
    path('detalleAvion/<pk>/', AvionDetail.as_view(), name="DetalleAvion"),
    path('creaAvion/', AvionCreate.as_view(), name="CreaAvion"),
    path('actualizarAvion/<pk>/', AvionUpdate.as_view(), name="ActualizaAvion"),
    path('eliminarAvion/<pk>/', AvionDelete.as_view(), name="EliminaAvion"),
    path('login/', loginView, name="Login"),
    path('registrar/', register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
]