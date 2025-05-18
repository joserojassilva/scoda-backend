from django.db import models
from usuarios.models import Usuario
from ubicacion.models import Comuna

class Apoderado(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='apoderado')
    nombres = models.CharField(max_length=100)
    apellido_uno = models.CharField(max_length=100)
    apellido_dos = models.CharField(max_length=100, blank=True, null=True)
    run = models.CharField(max_length=10)
    dv = models.CharField(max_length=2)
    fecha_nacimiento = models.DateField()
    fono = models.IntegerField(blank=True, null=True)
    fono_dos = models.IntegerField(blank=True, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'apoderado'
        verbose_name_plural = "apoderados"


    def __str__(self):
        return f'{self.nombres} {self.apellido_uno}'
    
class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='profesor')
    nombres = models.CharField(max_length=100)
    apellido_uno = models.CharField(max_length=100)
    apellido_dos = models.CharField(max_length=100, blank=True, null=True)
    run = models.CharField(max_length=10)
    dv = models.CharField(max_length=2)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'profesor'
        verbose_name_plural = "profesores"

    def __str__(self):
        return f'{self.nombres} {self.apellido_uno}'
