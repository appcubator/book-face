

from django.test import TestCase
from django.test.client import Client
from webapp.models import User


class StaticPagesTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_homepage(self):
        r = self.c.get('/')
        self.assertIn(r.status_code, (200, 302))
