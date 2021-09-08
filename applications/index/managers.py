from django.db import models
from django.db.models import Q


#
class PublicacionManager(models.Manager):

    def listarPublicacion(self, busqueda):
        lista = self.filter(
            planta_Pub__nombre_Planta__icontains=busqueda,
        )
        return lista

    def listarPublicacionByUser(self, user, busqueda):
        lista = self.filter(
            Q(usuario__exact=user),
        )
        lista = lista.filter(
            Q(planta_Pub__nombre_Planta__icontains=busqueda),
        )
        return lista

    def createPublicacion(self, fotografia_Pub, planta_Pub, lugar_Sembrada_Pub, fecha_Sembrada, sombra, sol, cuidados,
                          usuario):
        Publicacion = self.model(
            fotografia_Pub=fotografia_Pub,
            planta_Pub=planta_Pub,
            lugar_Sembrada_Pub=lugar_Sembrada_Pub,
            fecha_Sembrada=fecha_Sembrada,
            sombra=sombra,
            sol=sol,
            cuidados=cuidados,
            usuario=usuario
        )
        Publicacion.save(using=self.db)
        return Publicacion


class PlantasManager(models.Manager):

    def listarPlantas(self, busqueda):
        lista = self.filter(
            nombre_Planta__icontains=busqueda,
        )
        return lista

    def createPlanta(self, nombre_Planta, tipo_Planta, dimension_Planta):
        Planta = self.model(
            nombre_Planta=nombre_Planta,
            tipo_Planta=tipo_Planta,
            dimension_Planta=dimension_Planta
        )
        Planta.save(using=self.db)
        return Planta
