from django.contrib import admin

from .models import Job, JobLanguageSkill, JobTopicSkill
# Register your models here.

admin.site.register(Job)
admin.site.register(JobLanguageSkill)
admin.site.register(JobTopicSkill)