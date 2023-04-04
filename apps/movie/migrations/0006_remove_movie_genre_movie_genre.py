# Generated by Django 4.1.7 on 2023-04-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_visitcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movie.genre'),
        ),
    ]
