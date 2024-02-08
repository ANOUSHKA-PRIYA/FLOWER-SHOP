# flowerbloom/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('signup/', views.signup, name='signup-page'),
    path('login/', views.login_view, name='login-page'),
    path('about/', views.about, name='about-page'),    
    path('profile/', views.profile, name='profile-page'),    
    path('allcart/', views.view_cart, name='cart-page'),    
    path('category/', views.category, name='category-page'),
    path('address/', views.address, name='address-page'),    
    path('orders/', views.orders, name='orders-page'),    
    path('setting/', views.setting, name='setting-page'),    
    path('wishlist/', views.wishlist, name='wishlist-page'),    
    path('signout/', views.signout, name='signout-page'),
    path('add_to_cart/<int:p_id>/', views.add_to_cart, name='add_to_cart'),    
    path('allCart/', views.view_cart, name='allcart-page'),    
    path('remove/<int:id>/', views.remove_cart, name='remcart-page'),
    path('product/<int:p_id>/', views.product, name='product'),
]


'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('', home, name='home'),
    #path('category/', views.category, name='category'),
    # Add more paths for other pages if needed
]'''