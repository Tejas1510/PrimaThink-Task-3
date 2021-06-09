from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    return render(request, 'home.html', {})
    
def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = authenticate(email=email, password=password)
        print('USER: ', str(user),"Email: ",email, "password: ", password)
        if user is not None and user.is_active:
            # Login Successfull
            login(request, user)
            return redirect('home')
        else:
            # Login Unsuccessfull , Show Same Page With Error
            return render(request, 'login.html', {'loginStatus':"Incorrect Credentials."})
    else:
        if request.user.is_authenticated:
            # If user is already logged in, send to home
            return redirect('home')
        # Display Login Page
        return render(request, 'login.html', {})
