from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if(request.user.id==None):
        return HttpResponse("Please login.")
    return HttpResponse("Welcome %s" % request.user)