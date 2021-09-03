from django.db import models


#
class PublicacionManager(models.Manager):

    def listarPublicacion(self, busqueda):
        lista = self.filter(
            planta_Pub__nombre_Planta__icontains=busqueda,
        )
        return lista
