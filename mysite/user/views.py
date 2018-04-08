from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("hi")

def detail(request, user_id):
    return HttpResponse(user_id)

def me(request):
    return redirect('/user/' + str(request.user.id))