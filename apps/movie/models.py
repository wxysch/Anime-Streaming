from django.db import models
from django.core.validators import FileExtensionValidator

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
    restrictions = models.CharField(max_length=50)
    popular = models.BooleanField(default=False,blank=True,null=True)
    liveaction = models.BooleanField(default=False,blank=True,null=True)
    typeof = models.CharField(max_length=255)
    studio = models.CharField(max_length=255)
    dateAired = models.CharField(max_length=150)
    status = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    visitcount = models.IntegerField(default=0) 
    scores = models.BigIntegerField(default=0)
    rating = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Полнометражный'
        verbose_name_plural = 'Полнометражные'

class Video(models.Model):
    title = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'