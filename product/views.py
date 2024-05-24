from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product



class HomeView(ListView):

    model = Product
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["recent"] = Product.objects.all()[:5]
        return context

class CategoryListView(ListView):

    model = Category
    template_name = 'product/category_list.html'

class ProductListView(ListView):

    model = Product
    template_name = 'product/product_list.html'

class ProductDetailView(DetailView):

    model = Product
    template_name = 'product/product_detail.html'

    def get_object(self):

        id = self.kwargs.get('id')
        return get_object_or_404(Product.objects.all(), pk=id)
