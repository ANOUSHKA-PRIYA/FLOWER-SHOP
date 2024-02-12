
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
    path('puja/', views.puja, name='puja-page'),
    path('valentine/', views.valentine, name='valentineday-page'),
    path('anniversary/', views.anniversary, name='anniversary-page'),
    path('cactus/', views.cactus, name='cactus-page'),
    path('gift/', views.gift, name='gift-page'),
    path('plant/', views.plant, name='plant-page'),
    path('marriage/', views.marriage, name='marriage-page'),
    path('address/', views.address, name='address-page'),    
    path('orders/', views.orders, name='orders-page'),    
    path('setting/', views.setting, name='setting-page'),    
    path('wishlist/', views.wishlist, name='wishlist-page'),    
    path('signout/', views.signout, name='signout-page'),
    path('add_to_cart/<int:p_id>/', views.add_to_cart, name='add_to_cart'),    
    path('allCart/', views.view_cart, name='allcart-page'),    
    path('remove/<int:id>/', views.remove_cart, name='remcart-page'),
    path('product/<int:p_id>/', views.product, name='product'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('payment-success/', views.payment_success,name='payment-success'),
    path('initiate-payment/', views.initiate_payment,name='initiate_payment'),
    path('payment-failed/', views.payment_failed,name='payment-failed'),
    path('payment-policies/', views.payment_policies,name='payment-policies'),
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