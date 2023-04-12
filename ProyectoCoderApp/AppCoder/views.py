from django.shortcuts import render
from .models import Avion
from django.http import HttpResponse
from .forms import AvionFormulario

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
    return render(request, "AppCoder/busquedaMatricula.html")

def buscar(request):
    # respuesta = f'Estoy buscando la matricula nro: {request.GET['matricula']}'

    if request.GET["matricula"]:
        matricula = request.GET["matricula"]
        avion = Avion.objects.filter(matricula_icontains=matricula)

        return render(request, "App/Codder/resultadosBusquedas.html", {"avion": avion, "matricula": matricula})
    else:
        respuesta ="No enviaste datos"

    return HttpResponse(respuesta)