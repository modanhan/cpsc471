"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm



urlpatterns = [
    path('polls/', include('polls.urls')),
    path('challenge/', include('challenge.urls')),
    path('user/', include('user.urls')),
    path('language/', include('language.urls')),
    path('topic/', include('topic.urls')),
    path('home/', include('home.urls')),
    path('job/', include('job.urls')),
    path('company/', include('company.urls')),
    
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/home/',
    )),
]