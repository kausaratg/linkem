from django.shortcuts import render, redirect
from authentication.forms import RegistrationForm, LoginForm
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            messages.error(request, "Username already Exist!")
            return redirect('register')
        if User.objects.filter(email = email):
            messages.error(request, "Email already Exist!")
            return redirect('register')
        if password1 != password2:
            messages.error(request, "Password does not match!")
            return redirect('register')
        user = User.objects.create_user(username, email, password1)
        user.save()
        auth.login(request, user)
        messages.success(request,'Your Account Is Successfully Created')
        return redirect('/')
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
                messages.success(request, "Login successful")
                return redirect('/')
            messages.error(request, "Invalid Username or Password")
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, "registration/login.html", {"form":form})
    
def logout(request):
    auth.logout(request)
    messages.success(request, "successfully logout")
    return redirect('/')




