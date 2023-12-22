"""
URL Configuration for baking
"""
from django.urls import path
from . import views   # import views from app

app_name = "baking"

urlpatterns = [
    path('', views.home, name='home'),
    # add url patterns for the baking app here

    # Examples:
    # path('thing', views.thing, name='thing'),
]
