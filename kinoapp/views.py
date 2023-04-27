from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    rows = Products.objects.all()[0:6]

    context = {
        'title':'index',
        'rows': rows
    }
    return render(request, 'kinoapp/index.html', context)

def blog(request):
    rows = OurBlog.objects.all()

    context = {
        'title':'blog',
        'rows': rows
    }

    return render(request, 'kinoapp/blog.html',context)

def news(request):

    rows = News.objects.all()

    context = {
        'title':'news',
        'rows': rows,
    }

    return render(request, 'kinoapp/news.html',context)

def newsDetails(request, id):

    rows = NewsDetails.objects.filter(newsObject__id=id)

    context = {
        'title':'news',
        'rows': rows,
    }

    return render(request, 'kinoapp/blog-details.html',context)

def animeDetail(request, id):

    item = Products.objects.get(id=id)

    context = {
        'title':'news',
        'row': item,
    }

    return render(request, 'kinoapp/anime-details.html',context)

def signup(request):
    return render(request,'kinoapp/signup.html')