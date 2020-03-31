from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    """Set user profiles with modifiable host bio data."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(default="write your dang bio", blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=200, blank=True)
    display_host = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('update_host', args=[str(self.id)])

    def __str__(self):
        return self.first_name
