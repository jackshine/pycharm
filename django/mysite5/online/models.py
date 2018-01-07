from django.db import models

# Create your models here.
class User(models.Model):
    mobile = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
