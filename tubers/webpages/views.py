from django.shortcuts import render
from .models import Slider, Team, About
from youtubers.models import Youtuber
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by(
        '-created_date').filter(is_featured=True)

    all_youtubers = Youtuber.objects.order_by(
        '-created_date')[:6]  # [:6] -> trimming list to first 6

    data = {
        'sliders': sliders, 'teams': teams,
        'featured_youtubers': featured_youtubers,
        'all_youtubers': all_youtubers
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    about = About.objects.order_by('created_date')
    teams = Team.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'about': about,
    }
    return render(request, 'webpages/about.html', data)


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')
