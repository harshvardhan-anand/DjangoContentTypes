from django.urls import path
from . import views

app_name = 'drones'

urlpatterns = [
    path('', views.home, name='home'),
]