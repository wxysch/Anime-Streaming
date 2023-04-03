from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Movie(models.Model):
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='poster/')
    typeof = models.CharField(max_length=255)
    studio = models.CharField(max_length=255)
    dateAired = models.CharField(max_length=150)
    status = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    scores = models.BigIntegerField(default=0)
    rating = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'