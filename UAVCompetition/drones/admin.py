from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DroneCat)
admin.site.register(Drone)
admin.site.register(Pilot)
admin.site.register(Competition)