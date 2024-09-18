from django.db import models


# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.calle} {self.no_calle}'


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    donador = models.BooleanField()
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
