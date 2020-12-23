from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def allCustomers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'accounts/all_customers.html', context)

def customerList(request):
    all_customers = Customer.objects.all()
    customers = []
    for customer in all_customers:
        if customer.role == 'customer':
            customers.append(customer)


    context = {'customers': customers}
    return render(request, 'accounts/customers.html', context)


def guideList(request):
    all_customers = Customer.objects.all()
    guides = []
    for guide in all_customers:
        if guide == 'guide':
            guides.append(guide)
    context = {'guides': guides}
    return render(request, 'accounts/guides.html', context)


def createUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user=user, full_name=user.username)
            user.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/user-create.html', context)

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    context = {}
    return render(request, 'accounts/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('home')
