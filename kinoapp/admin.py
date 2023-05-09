from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(OurBlog)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(ProductsCategories)
admin.site.register(ProductsImages)
admin.site.register(Rating)
admin.site.register(Comments)
admin.site.register(News)
admin.site.register(NewsDetails)
admin.site.register(Slider)