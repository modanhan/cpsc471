from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=200)
    PARADIGM_CHOICES=(
        ('OO', 'Object Oriented'),
        ('FC', 'Functional'),
        ('OT', 'Other'),

    )
    paradigm = models.CharField(max_length=2, choices=PARADIGM_CHOICES, default='OO')