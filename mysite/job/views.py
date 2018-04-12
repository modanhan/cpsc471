from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Job
from django.contrib.auth.models import User
from topic.models import Topic, TopicRating
from language.models import Language, LanguageRating
from django.db.models import Q
import datetime
from company.models import Company

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    context={
        'jobs':jobs,
    }
    return render(request,'job/index.html',context)

def open(request):
    now = datetime.datetime.now()
    jobs=Job.objects.filter(openings__gt=0).filter(Q(expire_date__gte=now.date()))
    context={
        'jobs':jobs,
    }
    return render(request,'job/open.html',context)

def hasRequirement(user, tss,lss):
    good = True
    trs=user.topicrating_set.all()
    lrs=user.languagerating_set.all()
    for ts in tss:
        if not trs.filter(topic_id=ts.topic_id).exists():
            good=False
            break
        elif trs.get(topic_id=ts.topic_id).rating < ts.rating:
            good=False
            break
    for ls in lss:
        if not lrs.filter(language_id=ls.language_id).exists():
            good=False
            break
        elif lrs.get(language_id=ls.language_id).rating < ls.rating:
            good=False
            break
    return good

def detail(request, job_id):
    job=Job.objects.get(pk=job_id)
    tss=job.jobtopicskill_set.all()
    lss=job.joblanguageskill_set.all()

    tssview=[]
    for ts in tss:
        tssview.append((Topic.objects.get(pk=ts.topic_id), ts))
    lssview=[]
    for ls in lss:
        lssview.append((Language.objects.get(pk=ls.language_id), ls))


    users=User.objects.all()
    userviews=[]
    for user in users:
        if hasRequirement(user,tss,lss):
            userviews.append(user)

    qs='Log in to find out if you are qualified for this position!'
    if not request.user == None:
        qs= 'You are qualified!' if hasRequirement(request.user,tss,lss) else 'You are not qualified.'

    status='Open!'
    if job.openings == 0:
        status='Closed.'
    now = datetime.datetime.now()
    if job.expire_date.date() < now.date():
        status='Expired.'

    cp=Company.objects.get(pk=job.company_id)

    context={
        'job':job,
        'tss':tssview,
        'lss':lssview,
        'users':userviews,
        'qs':qs,
        'status':status,
        'cp':cp,
    }
    return render(request, 'job/detail.html',context)