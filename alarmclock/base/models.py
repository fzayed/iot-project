from django.db import models
from django.contrib.auth.models import User

class Time(models.Model):
    time = models.CharField(max_length=5)

    def __str__(self):
        return self.time