from django.contrib import admin
from .models import Planta, DimensionPlanta, TipoPlanta, LugarPlanta, PublicacionesPlantas

# Register your models here.
admin.site.register(Planta)
admin.site.register(DimensionPlanta)
admin.site.register(TipoPlanta)
admin.site.register(LugarPlanta)
admin.site.register(PublicacionesPlantas)
