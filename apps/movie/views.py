from django.shortcuts import render
from apps.settings.models import Setting
from .models import Movie,Genre,Video
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

def all_movies(request):
    setting = Setting.objects.latest('id')
    movies = Movie.objects.all()
    context = {
        'setting' : setting,
        'movies' : movies,
    }
    return render(request, 'anime/all_movies.html',context)

def video_watch(request,id):
    movie = Movie.objects.get(id=id)
    video = Video.objects.get(id=id)
    context = {
        'video' : video,
        'movie' : movie,
    }
    return render(request,'anime/movie-watching.html',context)