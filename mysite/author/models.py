from django.db import models

from challenge.models import Challenge
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    challenge=models.ForeignKey(Challenge,on_delete=models.CASCADE)
    timestamp=models.DateTimeField('timestamp')