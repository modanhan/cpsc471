from django.shortcuts import render
from django.http import HttpResponse
from .models import Challenge
from django.shortcuts import render, get_object_or_404

from topic.models import ChallengeTopic, Topic

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