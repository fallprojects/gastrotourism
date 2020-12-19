from django.db import models


# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(blank=True, default='default.png')
    duration = models.DurationField()

    def __str__(self):
        return self.name

    class Meta:
       verbose_name= 'Тур'
       verbose_name_plural = 'Туры'

class MainPage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'