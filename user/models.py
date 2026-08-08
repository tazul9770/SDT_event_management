from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from cloudinary.models import CloudinaryField 

class CustomUser(AbstractUser):
    designation = models.CharField(max_length=50, blank=True, null=True)
    designation_related_something = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = CloudinaryField('profile_image', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


