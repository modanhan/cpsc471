from django.contrib import admin
from .models import Language, LanguageRating

# Register your models here.
admin.site.register(Language)
admin.site.register(LanguageRating)