"""Posts views"""

# Django
from django.shortcuts import render

# Create your views here.
def list_posts(request):
    """List existing posts"""
    return render(request, 'posts/index.html')