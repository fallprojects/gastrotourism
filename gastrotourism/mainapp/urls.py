from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', tourList, name='tours'),
    path('tourorder/<int:tour_id>/', tourOrder, name='tourorder'),
    path('tour-detail/<int:tour_id>', tourDetail, name='tour-detail'),
    path('tourorders/', orderList, name='order-list'),
]

