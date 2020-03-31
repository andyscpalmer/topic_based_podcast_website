from django.test import TestCase, Client
from django.urls import reverse

from .models import Page

class HomepageTests(TestCase):

    def setUp(self):
        """Create dummy home page for tests"""
        home = Page.objects.create(title='Home', content='foo bar')
        self.response = self.client.get('/')

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Home')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hey! This is some nonsense that shouldnt be here')


class AboutPageTests(TestCase):

    def setUp(self):
        """Create dummy about page for tests"""
        home = Page.objects.create(title='About', content='foo bar')
        self.response = self.client.get('/about/')

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'About')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hey! This is some nonsense that shouldnt be here')
