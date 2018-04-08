from django.contrib import admin

# Register your models here.
from .models import Topic
from .models import ChallengeTopic

# Register your models here.
admin.site.register(Topic)
admin.site.register(ChallengeTopic)