from django.db import models
from django.forms import ModelForm

# Create your models here.
class Challenge(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    difficulty = models.IntegerField()

    def __str__(self):
        return self.name

class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = '__all__'