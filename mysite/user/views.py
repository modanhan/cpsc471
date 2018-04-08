from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("name")

def detail(request, user_id):
    user = User.objects.get(pk=request.user.id)
    return HttpResponse(user.first_name + ' ' + user.last_name)

def me(request):
    return redirect('/user/' + str(request.user.id))