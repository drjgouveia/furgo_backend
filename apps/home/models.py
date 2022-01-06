
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Log(models.Model):
    id = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=8)
    comb = models.CharField(max_length=64)
    kms = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
