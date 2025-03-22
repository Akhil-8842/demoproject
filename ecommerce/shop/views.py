from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shop.models import Category,Product


class Home(ListView):
    model = Category
    template_name = 'all_category.html'
    context_object_name = 'cat'

class CategoryDetails(DetailView):
    model = Category
    context_object_name = 'cat'
    template_name = 'products_page.html'


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'p'
    template_name = 'product_detail_page.html'






