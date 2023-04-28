from django.shortcuts import render
from .models import Avion, Piloto
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AvionFormulario, PilotoFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def avion(self, marca, matricula):
    avion = Avion(marca=marca, matricula=matricula)
    avion.save()

    return HttpResponse(f"""
    <p>Avion: {avion.marca} - Matricula: {avion.matricula} creados con éxito!</p>
    """)

def lista_avion(self):
    lista = Avion.objects.all()
    return render(self, "lista_avion.html", {"lista_avion": lista})

def inicio(self):
    return render(self, "inicio.html")

def avion(self):
    return render(self, "avion.html")

def piloto(self):
    return render(self, "piloto.html")

def pasajero(self):
    return render(self, "pasajero.html")

def planDeVuelo(self):
    return render(self, "planDeVuelo.html")

def avionFormulario(request):

    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = AvionFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            avion = Avion(marca=data['marca'], matricula=data['matricula'])
            avion.save()

            return render(request, "inicio.html")
        
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario Invalido"})
    
    else:

        miFormulario = AvionFormulario()

        return render(request, "avionFormulario.html", {"miFormulario": miFormulario})

def busquedaMatricula(request):
    return render(request, "busquedaMatricula.html")

def buscar(request):

    if request.GET["matricula"]:
        matricula = request.GET["matricula"]
        avion = Avion.objects.filter(matricula=matricula) # de la filmina--
    #     avion = Avion.objects.get(matricula=matricula)  del profe
        return render(request, "resultadosBusquedas.html", {"avion": avion, "matricula": matricula})
    else:
        return HttpResponse(f'No completaste el campo de la matricula')  

# @staff_member_required(login_url='/app-coder/')
def listaPilotos(request):
    pilotos = Piloto.objects.all()
    return render(request, "leerPilotos.html", {"pilotos": pilotos})


def crea_piloto(request):
    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
        miFormulario = PilotoFormulario(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            piloto = Piloto(nombre=data['nombre'], apellido=data['apellido'], rango=data['rango'])
            piloto.save()
            
            return HttpResponseRedirect('/app-coder/')

        else:
            return render(request, "inicio.html", {"mensaje": "Datos Invalidos"})
    else:
        miFormulario = PilotoFormulario()
        return render(request, "PilotoFormulario.html", {"miFormulario": miFormulario})

@login_required  
def eliminarPiloto(request, id):
    if request.method == 'POST':
        piloto = Piloto.objects.get(id=id)
        piloto.delete()

        pilotos = Piloto.objects.all()
        return render(request, "leerPilotos.html", {"pilotos": pilotos})
    
def editar_piloto(request, id):
    print('method: ', request.method)
    print('post: ', request.POST)

    piloto = Piloto.objects.get(id=id)

    if request.method == 'POST':
        miFormulario = PilotoFormulario(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            piloto.nombre = data['nombre']
            piloto.apellido = data['apellido']
            piloto.rango = data['rango']
            piloto.save()
            
            return HttpResponseRedirect('/app-coder/listaPilotos/')

        else:
            return render(request, "inicio.html", {"mensaje": "Datos Invalidos"})
    else:
        miFormulario = PilotoFormulario(initial={
            "nombre": piloto.nombre,
            "apellido": piloto.apellido,
            "rango": piloto.rango
        })
        return render(request, "editarFormulario.html", {"miFormulario": miFormulario, "id": piloto.id})
    

class AvionList(LoginRequiredMixin, ListView):
    model = Avion
    template_name = 'avion_list.html'
    context_object_name = 'avion'


class AvionDetail(DetailView):
    model = Avion
    template_name = 'avion_detail.html'
    context_object_name = 'avion'

class AvionCreate(CreateView):
    model = Avion
    template_name = 'avion_create.html'
    fields = ['marca', 'matricula']
    success_url = '/app-coder/listaAvion/'

class AvionUpdate(UpdateView):
    model = Avion
    template_name = 'avion_update.html'
    fields = ('__all__') #atajo para que me muestre todos los campos del atributo, en este caso matricula y marca
    success_url = '/app-coder/listaAvion/'
    context_object_name = 'avion'

class AvionDelete(DeleteView):
    model = Avion
    template_name = 'avion_delete.html'
    success_url = '/app-coder/listaAvion/'

def loginView(request):

    if request.method == 'POST':
        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(request, user)
                return render(request, 'inicio.html', {"mensaje": f'Bienvenido/a {usuario}'})
            
            else:
                return render(request, 'inicio.html', {"mensaje": f'Error: Los datos ingresados son invalidos o inexistentes'})

        else:
            return render(request, "inicio.html", {"mensaje": "Los datos ingresados son invalidos o inexistentes"})
    else:
        miFormulario = AuthenticationForm()
        return render(request, "login.html", {"miFormulario": miFormulario})

def register(request):
    if request.method == 'POST':
        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            username = data["username"]
            miFormulario.save()
            return render(request, 'inicio.html', {"mensaje": f'Usuario {username} creado con éxito!'})

        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        miFormulario = UserCreationForm()
        return render(request, "registro.html", {"miFormulario": miFormulario})