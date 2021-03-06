from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Challenge, ChallengeForm
from django.shortcuts import render, get_object_or_404

from author.models import Author
from topic.models import ChallengeTopic, Topic, TopicRating
from submission.models import Submission
from language.models import Language, LanguageRating
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
    challengeTopics = ChallengeTopic.objects.all().filter(challenge_id=challenge.id)

    language=Language.objects.all()
   
    topics = []
    for ct in challengeTopics:
        topics.append((Topic.objects.get(pk=ct.topic_id) ,ct.weight))

    context={
        'challenge':challenge,
        'language':language,
        'topics':topics
    }
    return render(request,'challenge/detail.html',context)

def submission(request, challenge_id):
    if request.user.id == None:
        return HttpResponse('Please log in.')
    if request.method == 'POST':
        try:
            requestpost = request.POST['choice']
        except:
            return HttpResponse('Please select a language.')
        c=Challenge.objects.get(pk=challenge_id)
        input = request.POST.get('your_solution', None)
        user=User.objects.get(pk=request.user.id)
        s=Submission()
        s.challenge=c
        l=Language.objects.get(pk=request.POST['choice'])
        s.language=l
        s.user=user
        s.timestamp=datetime.datetime.now()
        if c.ans == input:
            # check if never solved
            solve=Submission.objects.filter(user__id=request.user.id).filter(challenge__id=challenge_id).filter(result='AC')

            if not solve.exists():
                challengeTopics = ChallengeTopic.objects.all().filter(challenge_id=c.id)
                for ct in challengeTopics:
                    t=Topic.objects.get(pk=ct.topic_id)
                    tr,created=TopicRating.objects.get_or_create(topic=t, user=user, defaults={
                        'rating':0,
                        'timestamp':datetime.datetime.now(),})
                    if created:
                        tr.rating=0
                    tr.rating+=c.difficulty*ct.weight
                    tr.save()

            if not solve.filter(language__id=l.id).exists():
                lr,created=LanguageRating.objects.get_or_create(language=l, user=user, defaults={'rating':0,
                        'timestamp':datetime.datetime.now()})
                if created:
                    lr.rating=0
                lr.rating+=c.difficulty
                lr.save()

            s.result='AC'
            s.save()
            return redirect('correct/')
        else:
            s.result='WA'
            s.save()
            return HttpResponse('You are wrong!')
    else:
        return HttpResponse("Something's wrong.")

def create(request):
    topics = Topic.objects.all()
    if request.user.id == None:
        return HttpResponse('please login')
    if request.method == 'POST':
        requestpost = request.POST.getlist('choice')    # returns topic id
        requestweight = request.POST.getlist('weight')  # returns a list of weights
        form = ChallengeForm(request.POST)

        if form.is_valid():
            challenge = form.save(commit=False)
            exist = Challenge.objects.filter(name=challenge.name)
            if not exist.exists():
                challenge.save()

                a=Author()
                a.user = request.user
                a.challenge = challenge
                a.timestamp = datetime.datetime.now()
                a.save()
                
                for i in range(0, len(requestpost)):
                    idx = int(requestpost[i])
                    topicweight = 0
                    for j in range(0, len(requestweight)):
                        if requestweight[j] != '':
                            topicweight = requestweight[j]
                            requestweight[j] = ''
                            break

                    ct = ChallengeTopic()
                    ct.challenge = challenge
                    ct.topic = Topic.objects.get(pk=idx)
                    ct.weight = float(topicweight)
                    ct.save()

                return redirect('thanks/')
            else:
                return HttpResponse('Challenge Name exists')
    else:
        form = ChallengeForm()
        return render(request, 'challenge/create.html', {'form':form, 'topics':topics})

def thanks(request):
    return render(request, 'challenge/thanks.html', {})

def correct(request, challenge_id):
    return render(request, 'challenge/correct.html', {})