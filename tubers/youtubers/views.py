from django.shortcuts import get_object_or_404, render
from .models import Youtuber
from itertools import chain

# Create your views here.


def youtubers(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    cities = Youtuber.objects.values_list('city', flat=True).distinct()

    camera_types = Youtuber.objects.values_list(
        'camera_type', flat=True).distinct()

    categories = Youtuber.objects.values_list('category', flat=True).distinct()

    data = {
        'youtubers': youtubers,
        'cities': cities,
        'camera_types': camera_types,
        'categories': categories,
    }

    return render(request, 'youtubers/home.html', data)


def youtubers_detail(request, id):
    youtuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'youtuber': youtuber,
    }
    return render(request, 'youtubers/youtuber_details.html', data)


def search(request):
    youtubers = Youtuber.objects.order_by('-created_date')

    cities = Youtuber.objects.values_list('city', flat=True).distinct()

    camera_types = Youtuber.objects.values_list(
        'camera_type', flat=True).distinct()

    categories = Youtuber.objects.values_list('category', flat=True).distinct()

    crews = Youtuber.objects.values_list('crew', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            yt_name_search = youtubers.filter(name__icontains=keyword)
            yt_desc_search = youtubers.filter(description__icontains=keyword)
            youtubers = list(chain(yt_name_search, yt_desc_search))

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            youtubers = youtubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            youtubers = youtubers.filter(camera_type__iexact=camera_type)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            youtubers = youtubers.filter(category__iexact=category)

    if 'crew' in request.GET:
        crew = request.GET['crew']
        if crew:
            youtubers = youtubers.filter(crew__iexact=crew)

    data = {
        'youtubers': youtubers,
        'cities': cities,
        'camera_types': camera_types,
        'categories': categories,
        'crews': crews,
    }

    return render(request, 'youtubers/search.html', data)
