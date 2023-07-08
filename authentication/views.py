from django.shortcuts import render, redirect
from authentication.forms import RegistrationForm, LoginForm
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid:
            users = form.save()
            login(request, users )
            messages.success(request, "Registration successful")
            return redirect('/')
        messages.error(request, "invalid input. Please try again!!")
        return redirect("registration")
    else:
        form = RegistrationForm()
        return render(request, "registration/register.html", {"form":form})
    
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            messages.error(request, "Invalid Username or Password")
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, "registration/login.html", {"form":form})




