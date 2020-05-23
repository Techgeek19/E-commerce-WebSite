from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def index(request):
    # return HttpResponse("Home Page")
    obj= Product.objects.all()
    return render(request,'outlet/index.html', {'obj': obj})

def about(request):
    # return HttpResponse("About")
    return render(request,'outlet/about.html', {})


def contact(request):
    return HttpResponse("Contact")

def tracker(request):
    return HttpResponse("Tracker")

def search(request):
    return HttpResponse("Search")

def prodview(request):
    return HttpResponse("Product View")

def checkout(request):
    return HttpResponse("CheckOUT")

    