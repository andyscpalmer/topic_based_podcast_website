from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomuserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='grubbles',
            email='grubbles@email.com',
            password='testpass123',
            first_name='jon',
            last_name='podcaster',
            bio='i do podcasting',
            instagram='jonpodcaster',
            twitter='jonpodcaster6',
            website='www.jonpodcaster.com',
            display_host=True
        )
        self.assertEqual(user.username, 'grubbles')
        self.assertEqual(user.email, 'grubbles@email.com')
        self.assertEqual(user.first_name, 'jon')
        self.assertEqual(user.last_name, 'podcaster')
        self.assertEqual(user.bio, 'i do podcasting')
        self.assertEqual(user.instagram, 'jonpodcaster')
        self.assertEqual(user.twitter, 'jonpodcaster6')
        self.assertEqual(user.website, 'www.jonpodcaster.com')
        self.assertEqual(user.display_host, True)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
