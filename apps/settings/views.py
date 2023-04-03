from django.shortcuts import render
from .models import Setting,Slider
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    sliders = Slider.objects.all()
    context = {
        'setting' : setting,
        'sliders' : sliders,
    }
    return render(request,'anime/index.html',context)
