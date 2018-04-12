from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

app_name='job'

urlpatterns = [
    path('', views.index, name='index'),
    path('open/', views.open, name='open'),
    path('<int:job_id>/', views.detail, name='detail'),
]