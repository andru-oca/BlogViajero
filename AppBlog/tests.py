import random
import string

from django.test import TestCase
from AppBlog.models import Estudiante

class EstudianteTestCase(TestCase):

    def test_creacion_estudiantes(self):
        # Test 1: Comprobar puedo crear un estudiante con un nombre con letras random
        lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letras_apellido = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        nombre_prueba = "".join(lista_letras_nombre)
        apellido_prueba = "".join(lista_letras_apellido)
        estudiante_1 = Estudiante.objects.create(nombre=nombre_prueba, apellido=apellido_prueba)

        self.assertIsNotNone(estudiante_1.id)
        self.assertEqual(estudiante_1.nombre, nombre_prueba)
        self.assertEqual(estudiante_1.apellido, apellido_prueba)
