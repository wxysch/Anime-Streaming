from django.shortcuts import render
from apps.settings.models import Setting
from .models import News

# Create your views here.
def blog(request):
    setting = Setting.objects.latest('id')
    blog = News.objects.all()
    context = {
        setting : 'setting',
        blog : 'blog',
    }
    return render(request,'anime/blog.html',context)

def blog_details(request,id):
    setting = Setting.objects.latest('id')
    blog = News.objects.get(id=id)
    context = {
        setting : 'setting',
        blog : 'blog',
    }
    return render(request,'anime/blog-details.html',context)
