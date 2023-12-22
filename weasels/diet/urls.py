from django.urls import path
from . import views

app_name = 'diet'

urlpatterns = [
    path("", views.home, name="home"),
    path("toast", views.toast, name="toast"),
]