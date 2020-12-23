from django.http import HttpResponse
from django.shortcuts import render, redirect
from .decorator import allowed_roles

from .forms import *
from .models import *
# Create your views here.

def homePage(request):
    titles = MainPage.objects.all()
    context = {'titles': titles}
    return render(request, 'mainapp/home_page.html', context)


@allowed_roles(allowed=['manager'])
def orderList(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'mainapp/orders.html', context)


def tourList(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'mainapp/tours.html', context)


def tourDetail(request, tour_id):
    try:
        tour = Tour.objects.get(id=tour_id)
    except Tour.DoesNotExist:
        return HttpResponse('Page status = 404')
    form = TourDurationForm(initial={'tour': tour})
    if request.method == 'POST':
        form = TourDurationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'tour': tour, 'form': form}
    return render(request, 'mainapp/tour-detail.html', context)


def tourOrder(request, tour_id):
    try:
        tour = PreOrder.objects.get(id=tour_id)
    except Tour.DoesNotExist:
        return HttpResponse('Page status = 404')
    customer = request.user.customer
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tours')
    duration = tour.duration
    price = tour.tour.price
    total_price = duration * price
    context = {'form': form, 'total_ptice': total_price}
    return render(request, 'mainapp/tourorder.html', context)




