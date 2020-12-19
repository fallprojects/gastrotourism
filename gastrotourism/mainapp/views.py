from django.shortcuts import render
from .models import *
# Create your views here.

def tourList(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'mainapp/tours.html', context)

def homePage(request):
    titles = MainPage.objects.all()
    context = {'titles': titles}
    return render(request, 'mainapp/home_page.html', context)
