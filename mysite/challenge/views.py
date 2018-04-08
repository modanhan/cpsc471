from django.shortcuts import render
from django.http import HttpResponse
from .models import Challenge

# Create your views here.
def index(request):
    challenges = Challenge.objects.all()
    s = "Challenges\n"
    for c in challenges:
        s+=c.__str__()+"\n"
    return HttpResponse(s)