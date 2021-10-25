from django.db import models

# Create your models here.


class ImagenCarrusel(models.Model):
    nombre=models.CharField(max_length=20)
    imagen=models.ImageField(upload_to="carrusel/imagenes/")