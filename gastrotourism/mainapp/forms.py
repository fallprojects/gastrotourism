from django.forms import ModelForm
from .models import *

class TourForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['status']