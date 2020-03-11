from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class coordinates(models.Model):
    x_coordinate = models.CharField(max_length=100)
    y_coordinate = models.CharField(max_length=100)
  