from django.db import models

from challenge.models import Challenge
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ChallengeTopic(models.Model):
    challenge=models.ManyToManyField(Challenge, related_name='challenge')
    topic=models.ManyToManyField(Topic, related_name='topic')
    weight=models.FloatField()

class TopicRating(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    rating=models.IntegerField()
    timestamp=models.DateTimeField('timestamp')