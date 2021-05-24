from django.shortcuts import render


# Create your views here.
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'добро пожаловать на сайт',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    context = {'title': 'GeekShop - Каталог', 'header': 'GeekShop', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        context.update({'products': products})
    else:
        context.update({'products': Product.objects.all()})
    return render(request, 'mainapp/products.html', context)
