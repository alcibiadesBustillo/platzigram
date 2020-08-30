"""Platzigram URLS module"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls'), name='posts'),
    #path('posts/', include('posts.urls'), name='users'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
