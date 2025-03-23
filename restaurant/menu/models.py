

from django.db import models

# Define the Menu model
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Define the MenuItem model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    is_vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name
