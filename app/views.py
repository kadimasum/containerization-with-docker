from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("I am an app, I like containers")