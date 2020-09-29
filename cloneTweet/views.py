from django.shortcuts import render


# Module import
from .models import Tweet  # model class imported

# Method Link
from django.http import HttpResponse, Http404, JsonResponse

# Form Link
from .forms import TweetForm

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>WELCOME TO TWEET MAIN</h1>")
    return render(request, "pages/home.html", context={}, status=200)


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
        data["message"] = "This id doesn't exist"
        status = 404

    return JsonResponse(data, status=status)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    listTweet = [{"id": key.id, "content": key.content} for key in qs]
    data = {"response": listTweet}
    return JsonResponse(data)


def create_tweet_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        # do other form related logic
        obj.save()
        form = TweetForm()
    return render(request, "components/form.html", context={"form": form})
