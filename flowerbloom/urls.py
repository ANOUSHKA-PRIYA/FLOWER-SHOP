# flowerbloom/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('signup/', views.signup, name='signup-page'),
    path('login/', views.login_view, name='login-page'),

]