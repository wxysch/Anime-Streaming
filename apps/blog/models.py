from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='news_poster')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'