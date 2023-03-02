from django.db import models

class Usuario(models.Model):
    rut = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

