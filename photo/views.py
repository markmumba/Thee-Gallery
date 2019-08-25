from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from .models import Location,categories,Image
import datetime as dt

# Create your views here.

def home(request):
    pictures=Image.objects.all()

    return render(request,'index.html',{"image":image})






def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})
