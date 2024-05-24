from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path ('', views.HomeView.as_view(), name='home'),
    path ('product_list',  views.ProductListView.as_view(), name='product_list'),
    path ('produt_detail/<int:id>', views.ProductDetailView.as_view(), name='product_detail'),
    path ('category_list', views.CategoryListView.as_view(), name='category_list')
]

