from django.contrib import admin
from django.urls import path, include
from .views import tourList

urlpatterns = [
    path('', tourList, name='tours')
]
