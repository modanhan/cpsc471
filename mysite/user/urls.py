from django.urls import path

from . import views

app_name='user'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('me/', views.me, name='me'),
    path('<int:user_id>/authors/', views.authors, name='authors'),
    path('<int:user_id>/ratings/', views.ratings, name='ratings'),
]