from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Job
from django.contrib.auth.models import User
from topic.models import Topic, TopicRating
from language.models import Language, LanguageRating

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    context={
        'jobs':jobs,
    }
    return render(request,'job/index.html',context)

def detail(request, job_id):
    job=Job.objects.get(pk=job_id)

    users=User.objects.all()

    context={
        'job':job,
        'users':users,
    }
    return render(request, 'job/detail.html',context)