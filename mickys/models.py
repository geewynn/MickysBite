from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.IntegerField()

    def __str__(self):
        return self.user.username


class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=True)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.product_name






