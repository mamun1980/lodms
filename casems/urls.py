from django.contrib import admin
from django.urls import path


from .views import casems_home

urlpatterns = [
    path('case', casems_home),
] 

