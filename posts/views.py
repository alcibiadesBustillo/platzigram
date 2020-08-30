"""Posts views"""

# Django
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_posts(request):
    """List existing posts"""
    posts = [
        {
            'title': 'Mont Blac',
            'user': {
                'name': 'Alcy 1',
                'picture': 'https://picsum.photos/60/60/?image=1027'
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo' : 'https://picsum.photos/400/400/?image=1036'

        },
        {
            'title': 'Mont Blac 2',
            'user': {
                'name': 'Alcy 2',
                'picture': 'https://picsum.photos/60/60/?image=1005'
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo' : 'https://picsum.photos/400/400/?image=903'

        },
        {
            'title': 'Mont Blac 3',
            'user': {
                'name': 'Alcy 3',
                'picture': 'https://picsum.photos/60/60/?image=883'
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo' : 'https://picsum.photos/400/400/?image=1076'

        }
    ]
    return render(request, 'posts/index.html', {'posts': posts})