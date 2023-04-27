from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from kinoapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('news/', news, name='news'),
    path('newsDetail/<int:id>', newsDetails, name='newsDetails'),
    path('animeDetail/<int:id>', animeDetail, name='animeDetail'),
    path('signup/',signup,name="signup")
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)