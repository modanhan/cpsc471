from django.db import models

from challenge.models import Challenge
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=200)
    PARADIGM_CHOICES=(
        ('OO', 'Object Oriented'),
        ('FC', 'Functional'),
        ('OT', 'Other'),

    )
    paradigm = models.CharField(max_length=2, choices=PARADIGM_CHOICES, default='OO')

    def __str__(self):
        return self.name

class LanguageRating(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)
    rating=models.IntegerField()
    timestamp=models.DateTimeField('timestamp')