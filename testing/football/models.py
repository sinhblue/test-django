from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(maxlength=100)
