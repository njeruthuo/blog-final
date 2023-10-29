import requests
from .models import Blog


from django.test import TestCase
from django.contrib.auth.models import User


class TestBlogs(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(username="john", password="12345qwe")
        self.blog1 = Blog.objects.create(
            title="Title1", slug="slug1", author=self.user1, content="So much content", status="Published")

    def test_read_blog(self):
        response = requests.get('localhost:8000/read/')
        return self.assertEqual(self.blog1 == response)

    def test_update_blog(self):
        response = requests.get('localhost:8000/read/')
        return self.assertEqual(self.blog1 == response)

    def test_delete_blog(self):
        response = requests.get('localhost:8000/read/')
        return self.assertEqual(self.blog1 == response)

    def test_create_blog(self):
        response = requests.get('localhost:8000/read/')
        return self.assertEqual(self.blog1 == response)
