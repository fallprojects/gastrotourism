from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TourForm
from .models import *
# Create your views here.

def homePage(request):
    titles = MainPage.objects.all()
    context = {'titles': titles}
    return render(request, 'mainapp/home_page.html', context)

def orderList(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'mainapp/orders.html', context)


def tourList(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'mainapp/tours.html', context)

def tourOrder(request, tour_id):
    try:
        tour = Tour.objects.get(id=tour_id)
    except Tour.DoesNotExist:
        return HttpResponse('Page status = 404')
    customer = request.user.customer
    form = TourForm(initial={'tour': tour, 'customer': customer})
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tours')
    context = {'form': form, 'customer': customer}
    return render(request, 'mainapp/tourorder.html', context)


def tourDetail(request, tour_id):
    try:
        tour = Tour.objects.get(id=tour_id)
    except Tour.DoesNotExist:
        return HttpResponse('Page status = 404')
    customer = request.user
    form = TourForm(initial={'tour': tour, 'customer': customer})





