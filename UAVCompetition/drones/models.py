from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class DroneCat(models.Model):
    name = models.CharField(max_length=200)

class Drone(models.Model):
    name = models.CharField(max_length=200)
    dronecat = models.ForeignKey(DroneCat, on_delete=models.CASCADE, related_name='drones')
    created_at = models.DateTimeField(auto_now_add=True)

class Pilot(models.Model):
    name = models.CharField(max_length=200)

# https://stackoverflow.com/questions/67195137/how-to-create-several-contenttype-fields-in-a-django-model
class Competition(models.Model):
    name = models.CharField(max_length=200)
    
    # Content Type
    object_id = models.PositiveIntegerField()
    pilot_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='pilot')
    drone_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='drone')
    # Here you may prefer to use different object_id
    pilot = GenericForeignKey('pilot_content_type', 'object_id')
    drone = GenericForeignKey('drone_content_type', 'object_id')

    def __str__(self):
        return f"Pilot {self.pilot_content_type} registered for competition {self.name} with drone {self.drone}"
    
# Pilot A registered for Competition X with drone W