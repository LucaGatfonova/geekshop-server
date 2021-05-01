from django.shortcuts import render


# Create your views here.
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'добро пожаловать на сайт',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
