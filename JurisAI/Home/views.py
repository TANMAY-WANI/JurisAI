from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Service.models import Client


def index(request):
    if (request.user.is_anonymous):
        # print("Hello anonymous!!")
        return render(request,"auth.html",context={'route':'Login'})

    return redirect("api/service/chat")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username =username,password = password)
        if (user is not None):
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,"User does not exist. Try SignUp")
            
    return render(request,"auth.html",context={'route':'Login'})

def signup_user(request):
    if request.method == 'POST':
        print("Hello")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, username, password)
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            Client.create_user(username=username)
            login(request, user)
            return redirect("/")  # Use the name of the URL pattern for the index view

        
    return render(request,"auth.html",context={'route':"SignUp"})


def logout_user(request):
    logout(request)
    return redirect("/")