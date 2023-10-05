from django.db import models

# Create your models here.

class Especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    idUser = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    aPaterno = models.CharField(max_length=50)
    aMaterno = models.CharField(max_length=50)
    naciemiento = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
