"""Users views"""
# Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def loging_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:index')
        else:
            return render(request, 'users/login.html', {'error': 'Inavalid username and password'})
    return render(request, 'users/login.html')