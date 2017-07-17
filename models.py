from django.db import models

# Create your models here.


class Accounts(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)
    # score = models.IntegerField


class Missions (models.Model):
    id = models.IntegerField(primary_key=True)
    ownerid = models.IntegerField()
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    score = models.IntegerField()
    period = models.IntegerField()
