from django.db import models
from django.conf import settings
from django.utils.timezone import now
from datetime import datetime
from cloudinary.models import CloudinaryField 

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
    image = CloudinaryField('image', blank=True, null=True)
    date = models.DateField(default=now, blank=True,null=True)
    time = models.TimeField(default=current_time,blank=True, null=True)
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events")
    participant = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='event')

    def __str__(self):
        return f"{self.name} ({self.date})"

class RSVP(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} RSVPed to {self.event.name}"
