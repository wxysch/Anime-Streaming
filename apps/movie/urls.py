from django.urls import path
from .views import movie_detail,video_watch

urlpatterns = [
    path('movie-detail/<int:id>/',movie_detail,name='movie-details'),
    path('view/<int:id>/',video_watch,name='video'),
]