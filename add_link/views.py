from django.shortcuts import render, redirect
from add_link.forms import AddlinkForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    form = AddlinkForm()
    if request.method == "POST":
        form = AddlinkForm(request.POST)
        if form.is_valid():
            form_check = form.save(commit=False)
            form_check.username = request.user
            form_check.save()
            messages.success(request, "link saved successfully.")
            return redirect('/')
        messages.error(request, "Invalid input. Please try again")
        return redirect('/')
    return render(request, "add_link/index.html", {"form":form})