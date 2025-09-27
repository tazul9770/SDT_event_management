from django.db import models
from django.conf import settings
from django.utils.timezone import now
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
def current_time():
    return datetime.now().time()

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='event/image', blank=True, null=True)
    date = models.DateField(default=now, blank=True,null=True)
    time = models.TimeField(default=current_time,blank=True, null=True)
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events")
    participant = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='event')

    def __str__(self):
        return f"{self.name} ({self.date})"
