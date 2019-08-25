from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from .models import Location,categories,Image
import datetime as dt

# Create your views here.
def location(request,):
    date = dt.date.today()
    images = Image.location()
    return render(request, 'index.html', {"date": date,"images":images})

def australia(request):
    date = dt.date.today()
    images = Image.objects.filter(Location=3)
    return render(request, 'locations/australia.html', {"date": date,"images":images})

def hongkong(request):
    date = dt.date.today()
    images = Image.objects.filter(Location=1)
    return render(request, 'locations/hongkong.html', {"date": date,"images":images})

def africa(request):
    date = dt.date.today()
    images = Image.objects.filter(Location=2)
    return render(request, 'locations/africa.html', {"date": date,"images":images})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})
