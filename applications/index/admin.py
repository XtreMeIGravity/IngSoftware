from django.contrib import admin
from .models import Planta, CatDimensionPlanta, CatTipoPlanta, CatLugarPlanta, PublicacionesPlantas

# Register your models here.
admin.site.register(Planta)
admin.site.register(CatDimensionPlanta)
admin.site.register(CatTipoPlanta)
admin.site.register(CatLugarPlanta)
admin.site.register(PublicacionesPlantas)
