from django.shortcuts import render
from django.http import HttpResponse
from .models import Challenge
from django.shortcuts import render, get_object_or_404

from topic.models import ChallengeTopic, Topic
from submission.models import Submission
from language.models import Language
from django.contrib.auth.models import User

import datetime

# Create your views here.
def index(request):
    challenges = Challenge.objects.all()
    context={
        'challenges':challenges,
    }
    return render(request,'challenge/index.html',context)

def detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    challengeTopics = ChallengeTopic.objects.filter(challenge__id=challenge.id)

   
    topics = []
    for ct in challengeTopics:
        topics.append((Topic.objects.get(pk=ct.id), ct.weight))
    context={
        'challenge':challenge,
        'topics':topics
    }
    return render(request,'challenge/detail.html',context)

def submission(request, challenge_id):
    if request.user.id == None:
        return HttpResponse("Please log in.")
    if request.method == 'POST':
        c=Challenge.objects.get(pk=challenge_id)
        input = request.POST.get('your_solution', None)
        user=User.objects.get(pk=request.user.id)
        s=Submission()
        s.challenge=c
        l=Language.objects.all()[0]
        s.language=l
        s.user=user
        s.timestamp=datetime.datetime.now()
        if c.ans == input:
            s.result='AC'
            s.save()
            return HttpResponse('You are right!')
        else:
            s.result='WA'
            s.save()
            return HttpResponse('You are wrong!')
    else:
        return HttpResponse("Something's wrong.")