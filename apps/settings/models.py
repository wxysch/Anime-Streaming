from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='logo/')
    visitcount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class Slider(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='slider/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'