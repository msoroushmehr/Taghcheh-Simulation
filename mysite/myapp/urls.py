from django.contrib import admin
from django.urls import path
from .views import api
urlpatterns = [path('', api, name='api'),]