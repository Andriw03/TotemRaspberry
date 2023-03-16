from django.db import models

class Usuario(models.Model):
    rut = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

class Lugar(models.Model):
    nombreLugar = models.CharField(max_length=200)

class MCA(models.Model):
    descripcionMCA =models.CharField(max_length=200)
    idLugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)

class Flujo(models.Model):
    rutTrabajador = models.CharField(max_length=200)
    sentido = models.IntegerField()
    fechaHora = models.CharField(max_length=200)
    dirFoto = models.CharField(max_length=200)
    idMCA = models.ForeignKey(MCA, on_delete=models.CASCADE)