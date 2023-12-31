"""
    Views for the DJForms Project

    These are forms illustrating how forms work in Django
"""
from django.shortcuts import get_object_or_404, render
from .forms import DemoForm, HeroForm, HeroModel
from .models import Superhero

def home(request):
    """
    Welcome page

    :param request: HTTP request
    :return: HTTP Response
    """
    data = {
        'message': 'Welcome to the Django Forms Demo',
        'home_page': True,
    }
    return render(request, 'superheroes/home.html', data)


def demoform(request):
    """
    Generic form demo with various fields

    :param request: HTTP request
    :return: HTTP Response
    """
    invalid = False

    if request.method == 'POST':  # if form is bound (i.e., filled in)
        form = DemoForm(request.POST)
        if form.is_valid():  # passed validators and cleaners
            if form.cleaned_data.get('demo_char') == 'Barbie':
                invalid = True
            else:
                # if data is valid, show results page
                context = {
                        'page_title': 'Form Fields Results',
                        'data': form.cleaned_data,
                }
                return render(request, 'superheroes/form_results.html', context)
        else:
            # show form with errors for correcting
            invalid = True
    else:  # request method is GET
        form = DemoForm() # unbound (not filled in) form

    # unless POST/valid, redraw form
    context = {
        'page_title': 'Form Fields Example',
        'form': form,
        'invalid': invalid,
    }
    return render(request, 'superheroes/form_demo.html', context)


def heroform(request):
    """

    :param request: HTTP request
    :return: HTTP Response
    """

    # bound (filled-in) form
    if request.method == 'POST':
        form = HeroForm(request.POST)
        if form.is_valid():
            hero_name = form.cleaned_data['hero_name']
            hero_color = form.cleaned_data['hero_color']
            request.session['color'] = hero_color
            hero = get_object_or_404(Superhero, name=hero_name)
            context = {
                'page_title': 'Hero Details',
                'hero': hero,
                'color': hero_color,
            }
            return render(request, 'superheroes/hero_details.html', context)

    else:
        # unbound (empty) form
        form = HeroForm()

        context = {
            'page_title': 'Form Example',
            'form': form,
        }
        return render(request, 'superheroes/hero_select.html', context)


def heroadd(request):
    """

    :param request: HTTP request
    :return: HTTP Response
    """

    # bound (filled-in) form
    if request.method == 'POST':
        form = HeroModel(request.POST)
        if form.is_valid():
            form.save()  # write data to DB
            context = {
                'page_title': 'Hero Details',
                'name': form.cleaned_data['name'],
                'secret_identity': form.cleaned_data['secret_identity'],
                'real_name': form.cleaned_data['real_name'],
                'heroes': Superhero.objects.all(),
            }
            return render(request, 'superheroes/hero_model_results.html', context)
    else:
        # unbound (empty) form
        form = HeroModel()

        context = {
            'page_title': 'Form Example',
            'form': form,
        }
        return render(request, 'superheroes/hero_model_save.html', context)


def herolist(request):
    heroes = Superhero.objects.all()
    data = {'page_title': "Superheroes", 'heroes': heroes}
    return render(request, 'superheroes/hero_list.html', data)


def herodetails(request, hero_name):
    hero = get_object_or_404(Superhero, name=hero_name)
    data = {'hero': hero}
    return render(request, 'superheroes/hero_details.html', data)
