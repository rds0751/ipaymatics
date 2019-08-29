from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    refer = models.CharField(max_length=100)
    username= models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username
