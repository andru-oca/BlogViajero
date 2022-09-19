from cProfile import label
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

"""
Post (titulo, subtitulo, cuerpo, autor, fecha)
"""

class Post(models.Model):
    title = models.CharField(('Title'), max_length=50)
    subtitle = models.CharField(('Subtitle'), max_length=100)
    content = RichTextField(('Content of Post'), max_length=5000)
    image = models.ImageField(upload_to='post_images', null=True, blank = True)
    author = models.CharField(max_length=60)
    date = models.DateField()
    

    def __str__(self):
        return f'{self.titulo}, {self.subtitulo}'

class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"
