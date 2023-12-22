#from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to my Weasel Habitat App")

def spam(request):
    return HttpResponse("SPAM SPAM SPAM SPAM eggs SPAM")
