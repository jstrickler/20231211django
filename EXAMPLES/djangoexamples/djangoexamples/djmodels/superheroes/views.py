from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Superhero

def home(request):
    return HttpResponse("Welcome to the Superhero Database")

def hero_details(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero,
    }
    return render(request, 'superheroes/hero_details.html', data)
