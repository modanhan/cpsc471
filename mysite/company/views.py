from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Company
# Create your views here.
def index(request):
    cs=Company.objects.all()
    context={
        'cs':cs,
    }
    return render(request,'company/index.html',context)

def detail(request, company_id):
    c=Company.objects.get(pk=company_id)
    js=c.job_set.all()
    context={
        'c':c,
        'js':js,
    }
    return render(request,'company/detail.html',context)