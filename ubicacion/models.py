from django.db import models

from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    iso_3166_1_alpha3 = models.CharField(max_length=3)

    class Meta:
        db_table = 'pais'
        verbose_name_plural = "paises"

    def __str__(self):
        return self.nombre


class Region(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        db_table = 'region'
        verbose_name_plural = "regiones"

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comuna'
        verbose_name_plural = "comunas"

    def __str__(self):
        return self.nombre