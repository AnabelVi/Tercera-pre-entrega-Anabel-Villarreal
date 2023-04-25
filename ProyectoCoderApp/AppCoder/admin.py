from django.contrib import admin
from .models import Avion, PlanDeVuelo, Pasajero, Piloto

# Register your models here.

admin.site.register(Avion)
admin.site.register(PlanDeVuelo)
admin.site.register(Pasajero)
admin.site.register(Piloto)
