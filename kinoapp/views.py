from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    rows = Products.objects.all()[0:6]
    topViews = Products.objects.order_by("views")[::-1][0:6]

    slider = Slider.objects.order_by("queueNumber")

    context = {
        'title':'index',
        'rows': rows,
        'slider':slider,
        'topViews':topViews
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


from django.views.decorators.csrf import csrf_protect 
@csrf_protect 
def searhLogic(request):

    searchName = request.POST.get('searchName')
    searchName = searchName.lower()

    print(searchName)
    all = Products.objects.all()
    values = []

    for item in all:
        name = item.name.lower()
        description = item.description.lower()

        try:
            if name.index(searchName) != -1 or description.index(searchName) != -1:
                values.append(item)
        except:
            pass

    context = {
        'rows':values
    }

    return render(request, 'kinoapp/search.html', context)