import random
import string

from django.test import TestCase
from AppBlog.models import Post

# class PostTestCase(TestCase):

#     def test_creacion_posts(self):
#         # Test 1: Comprobar puedo crear un post con un nombre con letras random
#         lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
#         lista_letras_apellido = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
#         nombre_prueba = "".join(lista_letras_nombre)
#         apellido_prueba = "".join(lista_letras_apellido)
#         post_1 = Post.objects.create(nombre=nombre_prueba, apellido=apellido_prueba)

#         self.assertIsNotNone(estudiante_1.id)
#         self.assertEqual(estudiante_1.nombre, nombre_prueba)
#         self.assertEqual(estudiante_1.apellido, apellido_prueba)
