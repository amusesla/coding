from django.shortcuts import render


# Module import
from .models import Tweet  # model class imported

# Method Link
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>WELCOME TO TWEET MAIN</h1>")


def dynamic_route_url_view(request, num, *args, **kwargs):
    return HttpResponse(f"<h1>Hello {num}</h1>")
