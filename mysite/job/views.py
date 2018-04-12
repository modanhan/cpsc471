from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    context={
        'jobs':jobs,
    }
    return render(request,'job/index.html',context)

def detail(request, job_id):
    job=Job.objects.get(pk=job_id)
    context={
        'job':job,
    }
    return render(request, 'job/detail.html',context)