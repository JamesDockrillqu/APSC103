from django.shortcuts import render
import googlemaps
from .models import accountInfo
import json
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

def home(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', )


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid Information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def map(request):
    key = settings.GOOGLE_MAPS_API_KEY
    context = {
        'key': key,
    }
    return render(request, 'map.html', context)

# This is the attempt at collecting user input
