# Generated by Django 4.1.7 on 2023-04-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_restrictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='visitcount',
            field=models.IntegerField(default=0),
        ),
    ]