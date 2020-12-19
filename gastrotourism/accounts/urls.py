from django.urls import path, include
from accounts.views import *

urlpatterns = [
    path('', allCustomers, name='all_customers'),
    path('customers/', customerList, name='customers'),
    path('guides/', guideList, name='guides'),
    path('user-create/', createUser, name='user-create'),
    path('login,', auth, name='login'),
]

