from django.db import models
from django.contrib.auth.models import User

"""
Post (titulo, subtitulo, cuerpo, autor, fecha)
"""

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.CharField(max_length=5000)
    autor = models.CharField(max_length=60)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.titulo}, {self.subtitulo}'

class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"
