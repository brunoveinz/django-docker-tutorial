from django.test import TestCase
from app.models import Post


# este test importa un modelo hace un post para crear una instancia del modelo y luego comprueba los datos
class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My Title", description="Blurb", wiki="Post Body")
        self.assertEqual(post.title, "My Title")
        self.assertEqual(post.description, "Blurb")
        self.assertEqual(post.wiki, "Post Body")
