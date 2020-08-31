from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    webaccount = models.DecimalField(name="webaccount", default=25000, 
                                     decimal_places=2, max_digits=50)
    points = models.IntegerField(name="points", default=0)

