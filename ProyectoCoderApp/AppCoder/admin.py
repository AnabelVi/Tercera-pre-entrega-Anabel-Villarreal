from django.contrib import admin
from .models import Avion, PlanDeVuelo, Pasajero

# Register your models here.

admin.site.register(Avion)
admin.site.register(PlanDeVuelo)
admin.site.register(Pasajero)
