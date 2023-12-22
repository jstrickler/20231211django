"""
URL Configuration for frying
"""
from django.urls import path
from . import views   # import views from app

app_name = "frying"

urlpatterns = [
    path('', views.home, name='home'),

    # add url patterns for the frying app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
