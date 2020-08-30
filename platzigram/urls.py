"""Platzigram URLS module"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls'), name='posts'),
    path('users/', include('users.urls'), name='login'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
