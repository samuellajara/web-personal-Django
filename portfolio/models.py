from distutils.command.upload import upload
from enum import auto
from pyexpat import model
from django.db import models

# Create your models here.


class proyectos(models.Model):
    proyecto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = 'proyectos')
    url = models.URLField()

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'

    def __str__(self):
        return self.proyecto

    
