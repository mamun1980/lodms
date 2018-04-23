
from django.urls import path

from .views import testapp_home

urlpatterns = [
    path('testapp', testapp_home),
]
