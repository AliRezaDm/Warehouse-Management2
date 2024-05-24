from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'image_tag','name', 'category_to_str', 'type', 'size', 'price', 'sale_price')
    list_filter = (['id', 'price', 'sale_price'])
    search_fields = ('id', 'title', 'category_to_str')
    ordering = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'parent', 'name')
    list_filter = (['id', 'name', 'parent'])
    search_fields = ('id', 'name', 'parent')
    ordering = ['id']