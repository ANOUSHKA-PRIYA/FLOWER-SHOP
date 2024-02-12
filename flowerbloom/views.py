# flowerbloom/views.py

'''from django.shortcuts import render
from django.http import HttpResponse
from . forms import MyRegFrm


def home(request):
    return render(request, 'flowerbloom/signup.html')  # Use the correct template name
    '''

# flowerbloom/views.py
# flowerbloom/views.py
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from .forms import MyRegFrm,LoginFrm
from .models import Product, Cart
from .models import WishlistItem,Order
import razorpay
from django.conf import settings
from django.http import JsonResponse


def signup(request):
    if request.POST:
        form=MyRegFrm(request.POST)
        if form.is_valid():
            try:
              form.save()
              messages.success(request,'Your registration is sucessful')
            except Exception as e: 
                messages.error(request, e)     
    else:    
        form=MyRegFrm()
    return render(request,'flowerbloom/signup.html',{'form':form})

def home(request):
    products = Product.objects.all().order_by('?')[:12]
    
    context = {
        'products': products
    }
    return render(request, 'flowerbloom/home.html',context)

def login_view(request):
    if request.POST:
        form = LoginFrm(request=request,data=request.POST)
        if form.is_valid():
            uemail = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate( username=uemail, password=upass)
            if user is not None:
                login(request, user)
                return redirect('category-page')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginFrm()
    return render(request, 'flowerbloom/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/login/')

def add_to_cart(request, p_id):
    if request.user.is_authenticated:
        product = Product.objects.get(p_id=p_id)  # Retrieve the product using the p_id from the request
        cart_item, created = Cart.objects.get_or_create(product=product, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('/allcart/')
    else:
        return redirect('/login/')  # Redirect to login page if user is not authenticated

def view_cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        iprice = sum(item.product.price + item.product.delivery_charge for item in cart_items)
        total_price = sum((item.product.price + item.product.delivery_charge) * item.quantity for item in cart_items)
        return render(request, 'flowerbloom/cart.html', {'cart_items': cart_items, 'total_price': total_price,'iprice':iprice})
    else:
        return redirect('/login/') 

def remove_cart(request,id):
    if request.user.is_authenticated:
        cart_item = Cart.objects.get(id=id,user=request.user)
        cart_item.delete()
        return redirect('/allcart/')
    else:
        return redirect('/login/')


def about(request):
    return render(request, 'flowerbloom/about.html')

def profile(request):
    return render(request, 'flowerbloom/profile.html')

def category(request):
    if request.user.is_authenticated:
        birthday_products = Product.objects.filter(category__cat_name='Birthday Flowers')
        return render(request, 'flowerbloom/category.html', {'birthday_products': birthday_products})
    else:
        return redirect('/signin/')

def wishlist(request):
    return render(request, 'flowerbloom/wishlist.html')

def setting(request):
    return render(request, 'flowerbloom/setting.html')

def orders(request):
    return render(request, 'flowerbloom/orders.html')

def address(request):
    return render(request, 'flowerbloom/address.html')

def puja(request):
    if request.user.is_authenticated:
        puja_products = Product.objects.filter(category__cat_name='Puja Flowers')
        return render(request, 'flowerbloom/puja.html', {'puja_products': puja_products})
    else:
        return redirect('/signin/')

def valentine(request):
    if request.user.is_authenticated:
        valentine_products = Product.objects.filter(category__cat_name='Valentine day Flowers')
        return render(request, 'flowerbloom/valentine.html', {'valentine_products': valentine_products})
    else:
        return redirect('/signin/')
    
def plant(request):
    if request.user.is_authenticated:
        plant_products = Product.objects.filter(category__cat_name='Plants and Greenery')
        return render(request, 'flowerbloom/plant.html', {'plant_products': plant_products})
    else:
        return redirect('/signin/')
    
def cactus(request):
    if request.user.is_authenticated:
        cactus = Product.objects.filter(category__cat_name='Cactus Plants')
        return render(request, 'flowerbloom/cactus.html', {'cactus': cactus})
    else:
        return redirect('/signin/')
    
def marriage(request):
    if request.user.is_authenticated:
        marriage = Product.objects.filter(category__cat_name='Marriage Flowers')
        return render(request, 'flowerbloom/marraige.html', {'marriage': marriage})
    else:
        return redirect('/signin/')
    
def anniversary(request):
    if request.user.is_authenticated:
        anniversary = Product.objects.filter(category__cat_name='Anniversary Flowers')
        return render(request, 'flowerbloom/anni.html', {'anniversary': anniversary})
    else:
        return redirect('/signin/')
    
def gift(request):
    if request.user.is_authenticated:
        gift = Product.objects.all().select_related('category')
        return render(request, 'flowerbloom/gift.html', {'gift': gift})
    else:
        return redirect('/signin/')

def product(request, p_id):
    # Retrieve the product from the database based on the product ID
    product = get_object_or_404(Product, p_id=p_id)
    products = Product.objects.all().order_by('?')[:4]
    
    context = {
        'product': product,
        'products': products
    }
    return render(request, 'flowerbloom/product.html', context)

import os

def all_products(request):
    if request.user.is_authenticated:
        products_directory = os.path.join(settings.MEDIA_ROOT, 'products')
        filenames = os.listdir(products_directory)
        return render(request, 'flowerbloom/home.html', {'filenames': filenames})
    else:
        return redirect('/signin/')
    
def wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = WishlistItem.objects.filter(user=request.user)
        return render(request, 'flowerbloom/wishlist.html', {'wishlist_items': wishlist_items})
    else:
        return redirect('/signin/')


def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        WishlistItem.objects.get_or_create(user=request.user, product=product)
        return redirect('/wishlist/')
    else:
        return redirect('/signin/') 

def remove_from_wishlist(request, id):
    if request.user.is_authenticated:
        wishlist_item = WishlistItem.objects.get(id=id, user=request.user)
        wishlist_item.delete()
        return redirect('/wishlist/')
    else:
        return redirect('/signin/')


# def remove_cart(request,id):
#     if request.user.is_authenticated:
#         cart_item = Cart.objects.get(id=id,user=request.user)
#         cart_item.delete()
#         return redirect('/allcart/')
#     else:
#         return redirect('/login/')  

def initiate_payment(request):
    if request.method == "POST":

        amount = int(float(request.POST["amount"])) * 100  # Amount in paise
        address=request.POST['address']
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        payment_data = {
            "amount": amount,
            "currency": "INR",
            "receipt": "order_receipt",
            "notes": {
                "email": "user_email@example.com",
            },
        }

        order = client.order.create(data=payment_data)
        
        # Include key, name, description, and image in the JSON response
        response_data = {
            "id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "key": settings.RAZORPAY_API_KEY,
            "name": "My Project",
            "description": "Payment for Your Product",
            "image": "https://yourwebsite.com/logo.png",  # Replace with your logo URL
        }
        cart_items=Cart.objects.filter(user=request.user)
        # # payment_id=response_data.id
        for cart in cart_items:
            Order.objects.get_or_create(user=request.user, product= cart.product, quantity=cart.quantity, payment_status='success', address=address)
        
        Cart.objects.filter(user=request.user).delete()

        return JsonResponse(response_data)
    return redirect('flowerbloom:cart.html')

def payment_success(request):
    return render(request, 'flowerbloom/payment_success.html')


def payment_failed(request):
    return render(request, 'flowerbloom/payment_failure.html')

def payment_policies(request):
    return render(request, 'flowerbloom/payment_policies.html')