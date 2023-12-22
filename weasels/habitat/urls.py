from django.urls import path
from . import views

app_name = 'habitat'

urlpatterns = [
    path("", views.home, name="home"),
    path("spam", views.spam, name="spam"),
]