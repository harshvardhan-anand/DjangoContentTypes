from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    p = Pilot.objects.create(name='p1')
    dc = DroneCat.objects.create(name='dc1')
    d = Drone.objects.create(name ='d1', dronecat=dc)
    c = Competition.objects.create(name='c1', pilot=p, drone=d)
    c = Competition.objects.all()
    return render(request, 'home.html', {
        'c':c
    })