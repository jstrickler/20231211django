from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.

# example without template (only used in class -- always use templates in real life):
def home(request):
    return HttpResponse("Welcome to Frying")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to Frying" }
#     return render(request, 'frying/home.html', context)
