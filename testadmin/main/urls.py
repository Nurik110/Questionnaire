from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import login

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path("user/", views.user, name = "user"),
    path('result/', views.result, name='result'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
]