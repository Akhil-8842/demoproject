from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='media/cat_image', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='media/products', blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = ForeignKey(Category, on_delete=models.CASCADE,related_name="products")

    def __str__(self):
        return self.name
