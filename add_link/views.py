from django.shortcuts import render, redirect
from add_link.forms import AddlinkForm
from django.contrib import messages
from add_link.models import Add_link
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    links = Add_link.objects.filter(username = request.user)
    user = request.user
    context = {'links':links, "user":user}
    return render(request, "add_link/index.html", context)


def addlink_views(request):
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
    return render(request, 'add_link/form.html', {"form":form})

def generate_link(request, username):
    links = Add_link.objects.filter(username = request.user)
    user = request.user
    context = {'links':links, "user":user}
    return render(request, "add_link/generate_link.html", context)