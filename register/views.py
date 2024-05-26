from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def test(request):
    return render(request, 'authentication/test.html')

def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['name']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        # pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request, "Your account has been successfully created.")
        return render(request, "authentication/index.html")
    
    return render(request, "authentication/login1.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['Name']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/index.html')
        
        else:
            messages.error(request, "bad credentials")
            return redirect('home')
    
    
    return render(request, "authentication/login1.html")

def store(request):
    return render(request, "authentication/store.html")

def checkout(request):
    return render(request, "authentication/checkout.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

def add_to_cart(item):
    pass