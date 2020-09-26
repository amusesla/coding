from django.shortcuts import render


# Module import
from .models import Tweet  # model class imported

# Method Link
from django.http import HttpResponse, Http404, JsonResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>WELCOME TO TWEET MAIN</h1>")


# intro to dynamic ROUT URL
# def dynamic_route_url_view(request, num, *args, **kwargs):
#     return HttpResponse(f"<h1>Hello {num}</h1>")


# REST API VIEW
# which means these datas can be consumed by javaScrip, swift, etc
# return json data by using method - JsonResponse()


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {"id": tweet_id}

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
        status = 200
    except:
        data["message"] = "This id number doesn't exist"
        status = 404

    return JsonResponse(data, status=status)
