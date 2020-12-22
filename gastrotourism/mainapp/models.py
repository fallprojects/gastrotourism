from django.db import models


# Create your models here.
from accounts.models import Customer


class Tour(models.Model):
    durations = (('3 days', '3 days'),
                 ('5 dsys', '5 days'),
                 ('7 days', '7 days'))
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(blank=True, default='default.png')
    duration = models.CharField(max_length=20, choices=durations)
    price = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.duration


class MainPage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    statuses = (
        ('New order', 'New order'),
        ('In process', 'In process'),
        ('Finished', 'Finished')
    )
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=statuses, default='New order')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tour.name + ' ' + self.status

