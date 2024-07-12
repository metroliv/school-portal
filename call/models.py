
from django.db import models

class users(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    muted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
