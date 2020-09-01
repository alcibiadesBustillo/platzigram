from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loging_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('signup/', views.signup, name='signup'),
]
