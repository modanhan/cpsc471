from django.urls import path

from . import views

app_name='challenge'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:challenge_id>/', views.detail, name='detail'),
]