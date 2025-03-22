"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cart import views


app_name = 'cart'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.Register.as_view(), name="register"),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout, name="logout"),
    path('addtocart/<int:i>/',views.addtocart,name='addtocart'),
    path('cartview',views.cartview,name='cartview'),
    path('cart_decrement/<int:p>/',views.cart_decrement,name='cart_decrement'),
    path('cart_delete/<int:p>/', views.cart_delete, name='cart_delete'),
    path('add_category', views.AddCategory.as_view(), name='add_category'),
    path('add_product', views.AddProduct.as_view(), name='add_product'),
    path('add_stock/<int:pk>', views.AddStock.as_view(), name='add_stock'),
    path('add_billing_details', views.billingDetails, name='add_billing_details'),
    path('payment_status/<str:p>', views.paymentStatus, name='payment_status'),
    path('my_order', views.myOrders, name='my_order')

]
