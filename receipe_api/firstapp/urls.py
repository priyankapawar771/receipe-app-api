from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r'^greetings/',views.display)
]
