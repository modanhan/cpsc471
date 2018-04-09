from django.db import models

from django.contrib.auth.models import User
from language.models import Language
from challenge.models import Challenge

# Create your models here.
class Submission(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)
    challenge=models.ForeignKey(Challenge, on_delete=models.CASCADE)
    SUBMISSION_RESULT=(
        ('AC', 'Accepted'),
        ('WA', 'Wrong Answer'),
        ('TLE', 'Time Limit Exceeded'),
        ('MLE', 'Memory Limit Exceeded'),
        ('RT', 'Runtime Error'),
        ('UN', 'Unknown'),
    )
    result=models.CharField(max_length=3, choices=SUBMISSION_RESULT, default='UN')
    timestamp=models.DateTimeField('timestamp')
