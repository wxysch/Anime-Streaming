from django.shortcuts import render
from .models import Setting,Slider
from apps.movie.models import Movie,Genre
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    sliders = Slider.objects.all()
    movies = Movie.objects.all().order_by('?')
    context = {
        'setting' : setting,
        'sliders' : sliders,
        'movies' : movies,
    }
    return render(request,'anime/index.html',context)

    