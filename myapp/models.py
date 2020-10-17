from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Location(models.Model):
    latitude = models.FloatField()
    altitude = models.FloatField()

    def __str__(self):
        return f'{self.latitude} and {self.altitude}'


class Event(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=125)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EventMember(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event,related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name
