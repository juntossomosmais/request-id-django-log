import django
from django.test import Client, TestCase

django.setup()

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock


class RequestIDTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_middleware(self):
        response = self.c.get("/index/")

        self.assertTrue(response.has_header("HTTP_X_REQUEST_ID"))
