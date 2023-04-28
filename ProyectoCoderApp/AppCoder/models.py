from django.db import models

# Create your models here.
class Avion(models.Model):
    
    marca = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.marca} - {self.matricula}'

class Pasajero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

class Piloto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rango = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class PlanDeVuelo(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)

