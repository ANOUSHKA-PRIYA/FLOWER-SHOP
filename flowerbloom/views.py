# flowerbloom/views.py

'''from django.shortcuts import render
from django.http import HttpResponse
from . forms import MyRegFrm


def home(request):
    return render(request, 'flowerbloom/signup.html')  # Use the correct template name
    '''

# flowerbloom/views.py
# flowerbloom/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import MyRegFrm

def signup(request):
    if request.POST:
        form=MyRegFrm(request.POST)
        if form.is_valid():
            try:
              form.save()
              messages.success(request,'Your registration is sucessfully')
            except Exception as e: 
                messages.error(request, e)     
    else:
        form = MyRegFrm()

    # Update the template path
    return render(request, 'flowerbloom/signup.html', {'form': form})
def home(request):
    return render(request, 'flowerbloom/home.html')
def login_view(request):
    if request.method == 'POST':
        # Handle login logic
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login successful')
        else:
            return HttpResponse('Login failed')
    else:
        return render(request, 'flowerbloom/login.html')