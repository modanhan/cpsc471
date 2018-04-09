from django.contrib import admin

# Register your models here.
from .models import Topic
from .models import ChallengeTopic, TopicRating

# Register your models here.
admin.site.register(Topic)
admin.site.register(ChallengeTopic)
admin.site.register(TopicRating)