from django.db import models
from datetime import datetime

from users.models import User
# Create your models here.


class Vendor(models.Model):

    CLOTHING = 'CLOTHING'
    JEWELLERY = 'JEWELLERY'
    SHOES = 'SHOES'
    ART = 'ART'
    SERVICES = 'SERVICES'
    CATEGORY_CHOICES = [
        (CLOTHING, 'clothing'),
        (JEWELLERY, 'Jewellery'),
        (SHOES, 'Shoes'),
        (ART, 'Art'),
        (SERVICES, 'Service'),
    ]
    userId = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, blank=False)
    contact = models.CharField(max_length=100, unique=True, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    date_created = models.DateTimeField(default=datetime.now())


class Product(models.Model):
    productName = models.CharField(max_length=100, blank=False)
    vendorId = models.ForeignKey(
        Vendor, null=False, on_delete=models.CASCADE, related_name="product_of")
    price = models.IntegerField(null=False)
    description = models.TextField(max_length=400, blank=True)
    isDeliveryPossible = models.BooleanField(null=True)
    deliveryTime = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(default=datetime.now())


class ProductsImage(models.Model):
    productId = models.ForeignKey(
        Product, null=False, on_delete=models.CASCADE)
    imageOne = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    imageTwo = models.ImageField(blank=True,
                                 default='default.jpg', upload_to='profile_pics')
    imageThree = models.ImageField(blank=True,
                                   default='default.jpg', upload_to='profile_pics')
    imageFour = models.ImageField(blank=True,
                                  default='default.jpg', upload_to='profile_pics')
    imageFive = models.ImageField(blank=True,
                                  default='default.jpg', upload_to='profile_pics')
    imageSix = models.ImageField(blank=True,
                                 default='default.jpg', upload_to='profile_pics')

    class Meta:
        verbose_name_plural = "ProductsImages"
