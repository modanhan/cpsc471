from django.db import models
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    openings=models.IntegerField()
    pubish_date=models.DateTimeField('date published')
    expire_date=models.DateTimeField('expiration date')

