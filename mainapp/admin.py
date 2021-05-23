from django.contrib import admin

from mainapp.models import ProductCategory, Product
from authapp.models import User


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(ProductCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')
    readonly_fields = ('name',)
    search_fields = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email')
    ordering = ('username',)
    search_fields = ('name',)
