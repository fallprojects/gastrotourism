from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    roles = (('customer', 'customer'),
             ('guide', 'guide'))
    languages = (('English', 'English'),
                 ('Spanish', 'Spanish'),
                 ('Deutsch', 'Deutsch'),
                 ('French', 'French'),
                 ('Italian', 'Italian'))
    genders = (('male', 'male'),
               ('female', 'female'))

    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=roles)
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=6, choices=genders)
    image = models.ImageField(blank=True)
    language = models.CharField(max_length=8, blank=True, choices=languages, default='French')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

