from django.db import models

# Create your models here.

class Especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Sexo(models.Model):
    idSexo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    idUser = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50)
    aPaterno = models.CharField(max_length=50)
    aMaterno = models.CharField(max_length=50)
    nacimiento = models.DateField()
    password = models.CharField(max_length=20)
    especialidad = models.ForeignKey('Especialidad', on_delete=models.CASCADE, null=True)
    sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.email
    