

from django.test import TestCase
from django.test.client import Client
from webapp.models import Friendship, User, Wall_post


class StaticPagesTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_homepage(self):
        r = self.c.get('/')
        self.assertIn(r.status_code, (200, 302))

    def test_edit_profile(self):
        r = self.c.get('/Edit_profile/')
        self.assertIn(r.status_code, (200, 302))

    def test_all_users(self):
        r = self.c.get('/All_users/')
        self.assertIn(r.status_code, (200, 302))

    def test_newsfeed(self):
        r = self.c.get('/Newsfeed/')
        self.assertIn(r.status_code, (200, 302))

    def test_my_friends(self):
        r = self.c.get('/My_Friends/')
        self.assertIn(r.status_code, (200, 302))
