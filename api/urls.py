from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('user/', userAuth.as_view()),
]