from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)


class Match(models.Model):
    clubs = models.CharField(max_length=200)

    class Meta:
        db_table = "match"
