from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.contrib.auth.models import User

from author.models import Author

# Create your views here.
def index(request):
    users=User.objects.all()
    context={
        'users':users,
    }
    return render(request,'user/index.html',context)


def detail(request, user_id):
    user=User.objects.get(pk=user_id)
    context={
        'user':user,
    }
    return render(request,'user/detail.html',context)

def me(request):
    return redirect('/user/' + str(request.user.id))

def authors(request, user_id):
    user=User.objects.get(pk=user_id)
    authors=Author.objects.filter(user__id=user_id)
    challenges = []
    for a in authors:
        challenges.append(a.challenge)
    context={
        'user':user,
        'challenges':challenges,
    }
    return render(request,'user/authors.html',context)
