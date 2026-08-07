from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from cloudinary.models import CloudinaryField 

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


