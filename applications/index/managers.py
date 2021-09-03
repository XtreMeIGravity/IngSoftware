from django.db import models


#
class PublicacionManager(models.Manager):

    def createPublicacion(self, fotografia_Pub, planta_Pub, lugar_Sembrada_Pub, fecha_Sembrada, sombra, sol, cuidados):
        PublicacionesPlantas = self.model(fotografia_Pub=fotografia_Pub, planta_Pub=planta_Pub,
                                          lugar_Sembrada_Pub=lugar_Sembrada_Pub,
                                          fecha_Sembrada=fecha_Sembrada, sombra=sombra, sol=sol, cuidados=cuidados)
        PublicacionesPlantas.save(using=self.db)
        return PublicacionesPlantas
