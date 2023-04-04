from django.urls import path
from .views import movie_detail

urlpatterns = [
    path('movie-detail/<int:id>/',movie_detail,name='movie-details'),
]