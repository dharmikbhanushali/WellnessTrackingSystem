"""Test for swagger functionalities."""
# Django Libraries
from django.test import TestCase
from django.urls import reverse

# 3rd Party Libraries
from rest_framework import status
from rest_framework.test import APIClient


class PublicApiTests(TestCase):
    """Test access to `api/docs` api is accessible for public user."""

    def setUp(self):
        self.client = APIClient()

    def test_api_schema_generated_successfully(self):
        """Test if api schema is generated successfully"""
        url = reverse("api-schema")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_docs_accessible(self):
        """Test if both form of swagger api documentation is accessible"""
        url = reverse("api-docs")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        url = reverse("api-ReDocs")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
