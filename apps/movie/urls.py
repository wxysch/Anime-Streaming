from django.urls import path
from .views import movie_detail,video_watch,all_movies

urlpatterns = [
    path('movie-detail/<int:id>/',movie_detail,name='movie-details'),
    path('all_movies/',all_movies,name='all_movies'),
    path('view/<int:id>/',video_watch,name='video'),
]