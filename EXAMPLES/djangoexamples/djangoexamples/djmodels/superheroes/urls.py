"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views   # import views from app

app_name = "superheroes"

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:hero_name>/', views.hero_details, name="details"),
]
