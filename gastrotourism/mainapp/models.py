from django.db import models

# Create your models here.
from accounts.models import Customer


class MainPage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class Tour(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(blank=True, default='default.png')
    price = models.IntegerField()


    def __str__(self):
        return self.name


class PreOrder(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    durations = ((3, 3),
                 (5, 5),
                 (7, 7))
    duration = models.IntegerField(choices=durations)


class Order(models.Model):
    statuses = (
        ('New order', 'New order'),
        ('In process', 'In process'),
        ('Finished', 'Finished')
    )
    order = models.ForeignKey(PreOrder, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=statuses, default='New order')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tour.name + ' ' + self.status
