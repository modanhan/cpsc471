from django.db import models

from challenge.models import Challenge

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ChallengeTopic(models.Model):
    challenge=models.ManyToManyField(Challenge)
    topic=models.ManyToManyField(Topic)
    weight=models.FloatField()