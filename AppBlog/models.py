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
    image = models.ImageField(upload_to='post_images')
    author = models.CharField(max_length=60)
    date = models.DateField()
    
    def __str__(self):
        return f'{self.title}, {self.subtitle}'

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def save(self, *args, **kwargs):
        try:
            this = Post.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)

class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares')

    def __str__(self):
        return f"Imagen de: {self.user}"

    def save(self, *args, **kwargs):
        try:
            this = Avatar.objects.get(id=self.id)
            if this.imagen != self.imagen:
                this.imagen.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)
