
from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, MenuItem
from .forms import MenuItemForm

# View to display all items in a specific menu
def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    items = menu.items.all()  # Get all menu items related to the menu
    return render(request, 'menu_detail.html', {'menu': menu, 'items': items})

# View to update the price of a MenuItem
def update_item_price(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        new_price = request.POST.get('price')
        if new_price:
            item.price = new_price
            item.save()
            return redirect('menu_detail', menu_id=item.menu.id)
    return render(request, 'update_item_price.html', {'item': item})

# View to add a new MenuItem
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form': form})

# View to list all menus with their items
def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu_list.html', {'menus': menus})
