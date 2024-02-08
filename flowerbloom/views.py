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
    return render(request, 'flowerbloom/home.html')

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
        return render(request, 'flowerbloom/cart.html', {'cart_items': cart_items, 'total_price': total_price,'iprice':iprice })
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
        allprod = Product.objects.all().select_related('category')
        return render(request, 'flowerbloom/category.html', {'allprod': allprod})
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


'''def product(request, p_id):
    # Retrieve the product from the database based on the product ID
    product = get_object_or_404(Product, p_id=p_id)
    description= product.description.split('\n')
    return render(request, 'flowerbloom/product.html', {'product': product , 'description':description})'''

def product(request, p_id):
    # Retrieve the product from the database based on the product ID
    product = get_object_or_404(Product, p_id=p_id)
    return render(request, 'flowerbloom/product.html', {'product': product})