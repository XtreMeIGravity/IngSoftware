from django.db import models
from ckeditor.fields import RichTextField
from applications.users.models import User


# Create your models here.

class DimensionPlanta(models.Model):
    nombre_DimensionPlanta = models.CharField('DimensionPlanta', max_length=50)

    class Meta:
        verbose_name = "DimensionPlanta"
        verbose_name_plural = "DimensionPlantas"

    def __str__(self):
        return self.nombre_DimensionPlanta


class TipoPlanta(models.Model):
    nombre_TipoPlanta = models.CharField('TipoPlanta', max_length=50)

    class Meta:
        verbose_name = "TipoPlanta"
        verbose_name_plural = "TipoPlantas"

    def __str__(self):
        return self.nombre_TipoPlanta


class Planta(models.Model):
    nombre_Planta = models.CharField(max_length=50, unique=True)
    tipo_Planta = models.ForeignKey(TipoPlanta, on_delete=models.CASCADE)
    dimension_Planta = models.ForeignKey(DimensionPlanta, on_delete=models.CASCADE)

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + " " + self.apellidos


class LugarPlanta(models.Model):
    lugar_Planta = models.CharField('LugarPlanta', max_length=50)

    class Meta:
        verbose_name = "LugarPlanta"
        verbose_name_plural = "LugarPlantas"

    def __str__(self):
        return self.LugarPlanta


class PublicacionesPlantas(models.Model):
    fotografia_Pub = models.ImageField(upload_to='planta')
    planta_Pub = models.ManyToManyField(Planta)
    lugar_Sembrada_Pub = models.ForeignKey(LugarPlanta, on_delete=models.CASCADE)
    fecha_Sembrada = models.DateField()
    sombra = models.BooleanField()
    sol = models.BooleanField()
    cuidados = RichTextField(blank=True, null=True)

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + " " + self.apellidos
