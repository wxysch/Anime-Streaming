from django.shortcuts import render
from apps.settings.models import Setting
from .models import Movie,Genre
# Create your views here.
def movie_detail(request,id):
    setting = Setting.objects.latest('id')
    movie = Movie.objects.get(id=id)
    movie.visitcount = movie.visitcount + 1
    movie.save()
    context = {
        'setting' : setting,
        'movie' : movie,
    }
    return render(request, 'anime/movie-details.html',context)