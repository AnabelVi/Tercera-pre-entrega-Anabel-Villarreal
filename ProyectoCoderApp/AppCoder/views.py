from django.shortcuts import render
from .models import Avion, Piloto
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AvionFormulario, PilotoFormulario

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