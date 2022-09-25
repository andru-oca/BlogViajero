from datetime import datetime

from django.test import TestCase
from AppBlog.models import Post
from django.utils.crypto import get_random_string
import tempfile

class PostTestCase(TestCase):
    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):      
        # Declaración de variables de prueba
        title_test = get_random_string(length=50)
        subtitle_test = get_random_string(length=100)
        content_test = get_random_string(length=2000)
        image_test = tempfile.NamedTemporaryFile(suffix=".jpg").name
        author_test = get_random_string(length=60)
        date_test = datetime.now()

        # Creación de un post
        Post.objects.create(title=title_test, subtitle=subtitle_test, content=content_test, image=image_test, author=author_test, date=date_test)


    def test_title_label(self):
        # Test 1: Verifica si el label del campo coincide con el modelo
        post_test = Post.objects.get(id=1)
        field_label = post_test._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Title')


    def test_content_max_length(self):
        # Test 2: Verifica si el max_lenght del campo Content coincide con el modelo
        post_test = Post.objects.get(id=1)
        max_length = post_test._meta.get_field('content').max_length
        self.assertEqual(max_length, 5000)


    def test_object_name_is_title_comma_subtitle(self):
        # Test 3: Verifica si el __str__ del modelo coincide con "title, subtitle"
        post_test = Post.objects.get(id=1)
        expected_object_name = f'{post_test.title}, {post_test.subtitle}'
        self.assertEqual(str(post_test), expected_object_name)
