from django.test import TestCase
from django.urls import reverse


class SnacksAppTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse("List")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("List")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "_base.html")
