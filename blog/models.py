from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length = 50)
    contenido = models.CharField(max_length = 1000)
    imagen = models.ImageField(upload_to = 'blog', null = True, blank = True) # Post sin imagen OK
    autor = models.ForeignKey(User, on_delete= models.CASCADE) # Si un usuario se borra, sus post tambien
    categorias = models.ManyToManyField(Categoria) # Relacion N:N
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo
