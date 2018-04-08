from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    topics=Topic.objects.all()
    context={
        'topics':topics,
    }
    return render(request,'topic/index.html',context)