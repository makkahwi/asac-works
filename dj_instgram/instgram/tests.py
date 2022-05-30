from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TestPhotoView(TestCase):
    def setUp(self):
        self.client.login(username="writer", password="QwErTy123")

    def test_authetication_required(self):
        self.client.logout()
        url = reverse("Photo API List")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestCommentView(TestCase):
    def setUp(self):
        self.client.login(username="writer", password="QwErTy123")

    def test_authetication_required(self):
        self.client.logout()
        url = reverse("Comment API List")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
