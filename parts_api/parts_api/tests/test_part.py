import sqlite3
from parts_api import views
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

connection = sqlite3.connect("db.sqlite3")

class PartViewTests(APITestCase):
    def test_update_create_part(self):
        data = {
            "name": "test",
            "sku": "Example Movie",
            "description": "Example Story",
            "weight_ounces": 22,
            "is_active": 0
        }

        response = self.client.post(reverse('update', args=(1,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_part(self):
        data = {
            "is_active": 1
        }

        response = self.client.put(reverse('update', args=(1,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_get_part(self):
        response = self.client.get(reverse('update', args=(1,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_delete_part(self):
        response = self.client.delete(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_most_common_part(self):
        data = {
            'well': 3, 
            'has': 2, 
            'written': 1, 
            'to': 1, 
            'provide': 1
        }

        response = views.mostCommon("This portal has has well been created to provide well written well")
        self.assertEqual(response, data)


