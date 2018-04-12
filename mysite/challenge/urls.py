from django.urls import path

from . import views

app_name='challenge'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:challenge_id>/', views.detail, name='detail'),
    path('<int:challenge_id>/submission/', views.submission, name='submission'),
    path('<int:challenge_id>/submission/correct/', views.correct, name='correct'),
    path('create/', views.create, name='create'),
    path('create/thanks/', views.thanks, name='thanks'),

]