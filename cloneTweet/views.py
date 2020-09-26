from django.shortcuts import render


# Module import
from .models import Tweet  # model class imported

# Method Link
from django.http import HttpResponse, Http404


# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>WELCOME TO TWEET MAIN</h1>")


# intro to dynamic ROUT URL
# def dynamic_route_url_view(request, num, *args, **kwargs):
#     return HttpResponse(f"<h1>Hello {num}</h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f"Hello, id={tweet_id}. Your content is {obj.content}")
