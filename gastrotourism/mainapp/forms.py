from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['status']

class TourDurationForm(ModelForm):
    class Meta:
        model = PreOrder
        fields = '__all__'
        exclude = ['tour']

