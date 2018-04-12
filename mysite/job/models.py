from django.db import models
from django.utils import timezone

from topic.models import Topic
from language.models import Language

from company.models import Company

# Create your models here.
class Job(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    openings=models.IntegerField()
    pubish_date=models.DateTimeField('date published')
    expire_date=models.DateTimeField('expiration date')
    company=models.ForeignKey(Company, on_delete=models.CASCADE)

class JobTopicSkill(models.Model):
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    rating=models.IntegerField()

class JobLanguageSkill(models.Model):
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    language=models.ForeignKey(Language, on_delete=models.CASCADE)
    rating=models.IntegerField()
