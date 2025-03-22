from django.shortcuts import render
from django.db.models import Q
from shop.models import Product

# Create your views here.
def search(request):
    if(request.method == 'POST'):
        query = request.POST['q']
        items = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        context = {'prod':items}
    return render(request,'search.html',context)
