from django.shortcuts import render
from django.http import HttpResponse
from .models import Challenge
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    challenges = Challenge.objects.all()
    context={
        'challenges':challenges,
    }
    return render(request,'challenge/index.html',context)

def detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    context={
        'challenge':challenge,
    }
    return render(request,'challenge/detail.html',context)