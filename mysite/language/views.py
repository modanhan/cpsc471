from django.shortcuts import render

from .models import Language

# Create your views here.
def index(request):
    languages=Language.objects.all()
    context={
        'languages':languages,
    }
    return render(request,'languages/index.html',context)