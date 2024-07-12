from django.urls import path
from .views import mute, unmute, remove

urlpatterns = [
    path('mute/', mute, name='mute'),
    path('unmute/', unmute, name='unmute'),
    path('remove/', remove, name='remove'),
]
