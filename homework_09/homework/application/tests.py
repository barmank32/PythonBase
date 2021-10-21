from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from .models import Animal


class AppTests(TestCase):
    def setUp(self) -> None:
        Animal.objects.create(
            name="test1",
            kind="test1",
            age=5,
        )
        print("SetUp")

    def test_app_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print(response.content)

    def test_app_obj(self):
        resp = self.client.get(reverse("animal-list"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['object_list']), 1)

    def tearDown(self) -> None:
        Animal.objects.filter(name="test1").delete()
        print("tearDown")
