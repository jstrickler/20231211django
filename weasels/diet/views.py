from django.shortcuts import HttpResponse

# Create your views here.

def home(requests):
    return HttpResponse("Home page for Weasel diets")

def toast(requests):
    return HttpResponse("Nice toasty toast with a bit of Wemsleydale")

